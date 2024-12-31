
# End-to-End Text Summarizer Project 🚀

This repository provides an end-to-end machine learning pipeline for building a Text Summarizer using state-of-the-art transformer models. The project leverages Google Pegasus for abstractive summarization and integrates modular coding, CI/CD pipelines, Dockerization, and cloud-ready deployment on AWS.

## Key Features 🌟
- **Modular Code Structure**: Clear separation of data ingestion, validation, transformation, model training, and evaluation.
- **Transformer Model**: Fine-tuned Google Pegasus for abstractive text summarization.
- **Data Pipelines**: Automated workflows for training, testing, and validation.
- **CI/CD Integration**: Seamless deployment using GitHub Actions.
- **Cloud Deployment**: Ready-to-deploy on AWS with ECR and EC2.
- **Pythonic Standards**: Clean, well-documented, and reusable code.

## How to Run 🛠️

Follow the steps below to clone, set up, and run the project.

### Step 1: Clone the Repository
```bash
git clone https://github.com/therealmanraj/text-summariser-E2E-project.git  
cd text-summariser-E2E-project  
```

### Step 2: Set Up the Environment

#### For Mac/Linux (Python 3.8+ Recommended):
1. Ensure you have Python installed. Use `python3` and `pip3`.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv  
   source venv/bin/activate  
   ```
3. Verify the Python version:
   ```bash
   python --version  
   ```

#### For Windows:
1. Follow the same steps, but replace the activation command with:
   ```bash
   venv\Scripts\activate  
   ```

### Step 3: Install Requirements
Install all the dependencies listed in the `requirements.txt` file:
```bash
pip install --upgrade pip  
pip install -r requirements.txt  
```

### Step 4: Run the Application
Execute the pipeline using the main script:
```bash
python app.py  
```

### Step 5: Access Local Deployment
The project runs a server locally. Open your browser and navigate to:
```bash
http://127.0.0.1:5000  
```

## Deployment 🌐
The project is ready to deploy on any cloud provider. Here’s how:

1. **Update Configuration**: Modify `config.py` with your cloud settings (e.g., AWS, GCP, or Azure).
2. **Integrate CI/CD**: Add your cloud credentials to GitHub Actions workflows.
3. **Trigger Deployment**: Push to GitHub to initiate automated testing and deployment workflows.

### Deploy on AWS:
1. Create an ECR Repository and push the Docker image.
2. Launch an EC2 Instance and pull the Docker image.

## Author 👨‍💻
**Manraj Singh**

- **LinkedIn**: [Manraj Singh](#)
- **GitHub**: [therealmanraj](https://github.com/therealmanraj)

## License 📄
This project is licensed under the MIT License.
