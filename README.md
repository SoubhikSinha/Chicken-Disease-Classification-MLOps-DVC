# Chicken Disease Classification - MLOps - DVC

Acknowledgements
----
I would like to extend my sincere thanks to  [Krish Naik](https://github.com/krishnaik06)  and  [Bappi Ahmed](https://github.com/entbappy)  for their invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without their educational resources.

<br>
<br>

About the Project
---
This project focuses on exploring the principles of Python modular coding, MLOps (Machine Learning Operations, which applies DevOps practices to ML workflows), CI/CD (Continuous Integration, Continuous Delivery, and Continuous Deployment) pipelines using GitHub Actions, DVC (Data Version Control), and end-to-end project deployment on cloud platforms such as AWS (Amazon Web Services).<br>

The problem statement for this project is the classification of chicken diseases, specifically determining whether a chicken's fecal sample contains traces of "Coccidiosis" or indicates a healthy chicken.<br>

The VGG16 Convolutional Neural Network (CNN) architecture, a pre-trained model from the Keras library, was utilized through transfer learning. A Flask application was developed to deploy the model via a simple web interface. This application was deployed both locally and on AWS, demonstrating its versatility and scalability.

<br>
<br>

What I learned through this project ?
---
- <b>Modular Coding Practices using Python</b> 🔽<br>
Modular coding practices in Python involve structuring code into distinct, reusable, and manageable units (modules) to enhance readability, maintainability, and scalability. A program is divided into smaller, self-contained units, each focused on a specific functionality, allowing for independent development, testing, and maintenance. These modules can be grouped into packages, which are directories containing multiple related modules. Key principles include organizing code into functions and classes, adhering to the single-responsibility principle (each module focusing on one purpose), using meaningful names, and leveraging encapsulation to hide implementation details while exposing clear interfaces. Configuration files are used instead of hardcoding values, and tools like Python’s standard library and external libraries can simplify modularity. A well-structured directory, such as separating preprocessing, model logic, and Flask application routes into distinct packages, exemplifies this approach. This method improves code reusability, scalability, and collaboration while ensuring that changes in one module have minimal impact on others.

<br>
<br>

- <b>CI/CD (Continuous Integration and Continuous Delivery/Deployment)</b> 🔽<br>
**[CI/CD](https://about.gitlab.com/topics/ci-cd/)** is a set of practices and tools that automate and streamline the software development lifecycle. Continuous Integration focuses on regularly merging code changes into a shared repository, followed by automated testing to detect and address issues early. Continuous Delivery ensures that the codebase is always in a deployable state by automating the testing, building, and preparation of applications for deployment. Continuous Deployment takes this further by automatically deploying every code change to production once it passes all tests. Together, CI/CD fosters collaboration, reduces development cycles, improves code quality, and minimizes the risk of errors in production, enabling faster and more reliable software delivery.

<br>
<br>

- <b>GitHub Actions</b> 🔽<br>
**[GitHub Actions](https://github.com/features/actions)** is an integrated CI/CD platform within GitHub that automates tasks across the software development lifecycle. It enables developers to define workflows using YAML files, specifying triggers such as code pushes, pull requests, or scheduled events. These workflows can execute tasks like building, testing, and deploying code. GitHub Actions supports reusable components called actions, which can be shared and customized, along with native integration with GitHub repositories and third-party services. By providing a highly customizable, event-driven system, GitHub Actions simplifies automation, enhances collaboration, and accelerates the delivery of high-quality software directly from the repository.

<br>
<br>

- <b>DVC (Data Version Control)</b> 🌟 🔽<br>
**[DVC](https://dvc.org/)** is a powerful tool designed to bring the benefits of version control, like Git, into the world of data science and machine learning. It enables seamless tracking of datasets, models, and experiments, making collaboration on large-scale data projects as intuitive as managing code. Think of it as a bridge between reproducibility and agility : DVC allows you to version control massive datasets without cluttering your repository, linking data storage in remote locations like S3 or Google Drive. It also tracks the entire pipeline, ensuring every transformation or experiment is reproducible. With DVC, your projects gain clarity, teamwork becomes smoother, and scaling machine learning pipelines feels effortless—a game-changer for anyone working in data-driven environments.

<br>
<br>

How to run this project ?
---
### **1. Clone the Repository**

Clone the repository to your local machine :<br>
```bash
git clone https://github.com/SoubhikSinha/Chicken-Disease-Classification-MLOps-DVC.git
```

### **2. Create a Virtual Environment**

Navigate to the repository's root directory and create a Conda virtual environment :<br>
```bash
conda create --prefix ./venv python=3.11 -y
```

### **3. Activate the Conda Environment**
Activate the newly created environment :<br>
```bash
conda activate ./venv/
``` 

### **4. Install Required Libraries**
Install all the necessary dependencies :<br>
```bash
pip install -r requirements.txt
```

### **5. Remove Existing DVC-Related Files (If Any)**
Before running the project, delete the following files and directories :
-   `.dvc/`
-   `artifacts/`
-   `.dvcignore`
-   `dvc.lock`
-   `scores.json`

This ensures a fresh run without any conflicts or outdated configurations.

### **6. Run the Project (Without DVC)**
Run the project directly without using DVC :<br>
```bash
python main.py
```
<br>

**NOTE** : This will:
-   Automatically create the `artifacts/` folder.
-   Train the model and provide the results.  

If the `artifacts/` folder already exists, it will reprocess and retrain the model.

### **7. Run the Project (With DVC)**
To use DVC for managing pipelines, follow these steps :<br>
- **Initialize DVC**  
Initializes a DVC repository in the project :<br>
	```bash
	dvc init
	```

- **Reproduce the Pipeline**  
Runs or re-runs the pipeline, executing only the stages affected by changes in dependencies :<br>
	```bash
	dvc repro
	```

- **Visualize the Pipeline**  
Displays the pipeline’s dependency graph :<br>
	```bash
	dvc dag
	```

### **8. Viewing TensorBoard**
To view TensorBoard, run :<br>
```bash
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
```
Then navigate to the below in your browser :<br>

```bash
http://localhost:6006
```

### **9. Launch the Flask Application**
Start the Flask web application :<br>
```bash
python app.py
```

<br>

Open your browser and navigate to `http://localhost:8080` to interact with the application.<br>

To train the model from the browser, visit : `http://localhost:8080/train`.<br>

**NOTE** : Before running this, ensure the `artifacts/` folder is deleted for a fresh training session.
