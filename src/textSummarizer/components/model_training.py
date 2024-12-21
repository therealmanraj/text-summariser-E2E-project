from transformers import  TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset,load_from_disk
from textSummarizer.entity import ModelTrainingConfig
import torch    
import os
import wandb

class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        # Load the dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        # Use only a small subset of the dataset for testing
        small_train_dataset = dataset_samsum_pt["train"].shuffle(seed=42).select(range(5))  # First 100 samples
        small_eval_dataset = dataset_samsum_pt["validation"].shuffle(seed=42).select(range(1))  # First 50 samples
    
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            eval_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
        )
    
        trainer = Trainer(
            model=model_pegasus, 
            args=trainer_args,
            processing_class=tokenizer, 
            data_collator=seq2seq_data_collator,
            train_dataset=small_train_dataset, 
            eval_dataset=small_eval_dataset
        )
        
        os.environ["WANDB_MODE"] = "disabled"
        trainer.train()
    
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))