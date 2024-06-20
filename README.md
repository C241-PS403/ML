# Nusatala
See our prototype <a href="https://www.figma.com/proto/O9ASheCraA9sLiYyyVtHx4/Nusatala?type=design&node-id=73-873&scaling=scale-down&page-id=0%3A1&starting-point-node-id=14%3A813" title="Figma" target="_blank"><b>here</b></a>.

<br>


https://github.com/Nusatala/.github/assets/70735803/f0dd8ac1-5fe5-4a23-ac68-440a31aad20b


# Table of Content

- [Nusatala](#nusatala)
- [Table of Content](#table-of-content)
- [About Nusatala](#about-nusatala)
  - [Background](#background)
  - [Goal \& Aim](#goal--aim)
  - [Installation \& Deployment](#installation--deployment)
    - [Machine Learning - Project Installation to Personal Virtual Environment](#machine-learning---project-installation-to-personal-virtual-environment)
    - [Deploy Machine Learning Model with CloudRun on Google Cloud Platform](#deploy-machine-learning-model-with-cloudrun-on-google-cloud-platform)
    - [Mobile Development - Project Installation](#mobile-development---project-installation)
    - [Cloud Computing - Backend Project Installation](#cloud-computing---backend-project-installation)
  - [How Nusatala Works](#how-nusatala-works)
  - [Plans \& Realization](#plans--realization)
  - [Project Scope](#how-nusatala-works)
  - [Bibliography](#bibliography)
    - [A. Dataset](#a-dataset)
    - [B. Resources](#b-resources)
    - [C. Academic Papers](#c-academic-papers)
  - [Presentation](#presentation)
  - [Demo Video](#demo-video)
  - [Developers](#developers)

<br>

# About Nusatala

**Nusatala** is a mobile application that can recognize images of various traditional musical instruments and provide relevant information. This application will have image scanning, recommendations for nearby art communities, articles, quizzes, faq, user profiles, and traditional musical instrument store features.

![Nusatala Team](https://github.com/Nusatala/.github/assets/70735803/10205e94-1ed4-4fba-887a-89deb3b4c050)


## Background
Nusatala aims to enhance our knowledge of Indonesian traditional music instruments by using an app that can recognize images of these instruments and provide relevant information. Although there are apps available for learning about these instruments, they only offer limited info and cannot identify images using machine learning. Using an app that can identify images and provide relevant information, Nusatala can easily enhance our knowledge about Indonesian traditional music instruments in one convenient app.


## Goal & Aim


## Installation & Deployment
This step will explains how to install and deploy briefly :


####  Machine Learning - Project Installation to Personal Virtual Environment
1. Clone this repository
   ```bash
   git clone https://github.com/Nusatala/ML
   ```
2. Download the dataset <br>
  [Link dataset](https://drive.google.com/drive/folders/1zLFuIkJmukm16FtSIqsWWbHCP5JGhQkZ?usp=sharing)
3. Install All the Requirements Inside "requirements.txt"
  ```bash
   pip install -r requirements.txt
   ```
3. Make a new virtual environment using Python
   ```bash
   python -m venv nusatala-experimental
   ```
4. Activate the virtual environment
   ```bash
   env\Scripts\activate
   ```
5. Install All the Requirements Inside "requirements.txt"
   ```bash
   pip install -r requirements.txt
   ```
6. Go to folder Google-Cloud-Deploy to activate Flask web server
   ```bash
   cd Google-Cloud-Deploy
   ```
7. Run Flask
   ```bash
   flask run
   ```
8. Stop the application program or server by `ctrl + c`.


#### Mobile Development - Project Installation
1. Clone Repository
   ```bash
   git clone https://github.com/Nusatala/MD.git
   ```
2. Open the project using androd studio
3. Build project
4. Run on emulator or real device

#### Cloud Computing - Backend Project Installation
##### To start a project
1. Copy .env.example file and rename it to .env  
2. Fill that env with it's value
3. Install all dependencies, type:
    ```
    npm install
    ```
4. Create google cloud service account and add cloud storage admin role
5. Generate json key file from that account
6. Put the json key file to this project and rename it to "service-key.json"
7. To run this project, type:
    ```
    npm start
    ```
8. Run a migration
    ```
    npx prisma migrate dev --name init
    ```
9. Run a seeder
    ```
    npx prisma db seed
    ```

## How Nusatala Works
1. Nusatala app gets user image input with png, jpg, and jpeg format of traditional music instrument such as angklung, bonang, etc.
2. Convert the image to Numpy then normalized to 255 scale
3. Predict the image input using nusatala.h5 model that already build with ResNet and InceptionV3 pre-trained algorithm.
4. The predicted output is name of the traditional music instrument. The result must following the label in dataset, that are "Bonang", "Kolintang", "Rebab", "Saluang", "Sape", "Sasando", and "Tifa"
5. Finally, based on the traditional music instrument, system will render the regional origin, manufacture materials, history, tutorial to play the instrument video, and the community recommendation.

## Project Scope
- Data input for Indonesian traditional music instrument classification is an image
- Image formatted as JPG within size 150x150 pixels
- Classification only for Indonesian traditional music instrument
- On the first development, only using several classification on traditional music instruments.
- The store is just for recommendation, we do not provide an e-commerce system for buying and sell traditional music instruments.
- Art groups recommendation for learning traditional music instruments are based on Google Maps



## Plans & Realization
To keep on track, Nusatala team has been used Gantt Chart with Agile method. Additionally, Nusatala used to discuss for weekly sprint. Here is our Gantt Chart :

<a href="https://docs.google.com/spreadsheets/d/1LmzsixFD1n4JV55bvjUVj0eaERiUQOR7H_p-PQG4EGc/edit?usp=sharing" title="Nusatala Gantt Chart" target="_blank">Nusatala Gantt Chart</a>

![Timeline](https://github.com/Nusatala/.github/assets/70735803/e8e90c7b-5273-4694-b41a-43c2b71a7d0d)

![Gantt Chart](https://github.com/Nusatala/.github/assets/70735803/5ad668ea-2e64-4335-af0c-e364ca93128e)

![Trello](https://github.com/Nusatala/.github/assets/70735803/122b27e7-db75-4646-9d2d-d12dfb529287)


## Bibliography

### A. Dataset
Our dataset can be found here [Link dataset](https://drive.google.com/drive/folders/1zLFuIkJmukm16FtSIqsWWbHCP5JGhQkZ?usp=sharing).
### B. Resources
Tools/IDE/Library and resources that Nusatala use to build the app :
- IDE
  - <a href="https://code.visualstudio.com/" title="Visual Studio Code" target="_blank">
    <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white" />
  </a> &nbsp;
  - <a href="https://developer.android.com/studio?gclid=CjwKCAjwp6CkBhB_EiwAlQVyxRoFRkbXTQ0TrI0w-8LEwIttlMFbOnF-vTvc_e3dJFR55kiNIDo6nhoCMj8QAvD_BwE&gclsrc=aw.ds" title="Android Studio" target="_blank">
    <img src="https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white" />
- Library
  - Retrofit
  - <a href="https://www.tensorflow.org/" title="Tensorflow" target="_blank">
    <img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white" />
- Platform
  - <a href="https://colab.research.google.com/" title="Google Colaboratory" target="_blank">
    <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252" />
  - <a href="https://cloud.google.com/" title="Google Cloud Platform" target="_blank">
    <img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white" />
  - <a href="https://firebase.google.com/" title="Firebase" target="_blank">
    <img src="https://img.shields.io/badge/Firebase-039BE5?style=for-the-badge&logo=Firebase&logoColor=white" />
  - <a href="https://www.figma.com/" title="Figma" target="_blank">
    <img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white" />
  - <a href="https://flask.palletsprojects.com/en/2.3.x/" title="Flask" target="_blank">
    <img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" />
- API
  - Google APIs
- Project Management
  - <a href="https://discord.com/" title="Discord" target="_blank">
    <img src="https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white" />
  - <a href="https://workspace.google.com/" title="Google Workspace" target="_blank">
    <img src="https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=googledrive&logoColor=white" />
  - <a href="https://trello.com/" title="Trello" target="_blank">
    <img src="https://img.shields.io/badge/Trello-%23026AA7.svg?style=for-the-badge&logo=Trello&logoColor=white" />


### C. Academic Papers
- Hastawan, A.F. et al. (2019) ‘Designing Educational Game of Indonesian Traditional Musical Instruments Based on Android Using Unity 3D’, 379(Veic), pp. 92–100. Available at: https://doi.org/10.2991/assehr.k.191217.016.

  
## Presentation
Nusatala final presentation can be found here :

<a href="https://docs.google.com/presentation/d/1VwOp9IozLLFlN2vL-JvaJXI-YMvSX0hHble0yMn0lbA/edit?usp=sharing" title="Nusatala Presentation" target="_blank">
  <img src="https://github.com/Nusatala/.github/assets/70735803/bc2a165c-a742-4dd6-96ca-361a59a73ed6" alt="Jernihin Presentation Video" style="width: 500px">
</a>

[Link Presentation](https://docs.google.com/presentation/d/1VwOp9IozLLFlN2vL-JvaJXI-YMvSX0hHble0yMn0lbA/edit?usp=sharing)

## Demo Video
[Link Demo](bit.ly/Demo-Video-Nusatala)</br>
[Link Youtube](https://bit.ly/Video-Nusatala)

## Developers
 <a href="https://grow.google/intl/id_id/bangkit/?tab=machine-learning">Bangkit Academy led by Google, GoTo, and Traveloka 2023 Batch 1</a>
 
C23-PR552 Capstone Team - Nusatala

- [ML] M305DKX3952 - <a href="https://github.com/gunturajip" title="GitHub Guntur Aji Pratama" target="_blank">Guntur Aji Pratama</a>
- [ML] M169DSX1306 - <a href="https://github.com/Recovery018" title="GitHub Mochammad Iqbal Syaifurrahman" target="_blank">Mochammad Iqbal Syaifurrahman</a>
- [ML] M340DSY3395- <a href="https://github.com/faqirilmu31" title="GitHub Reni Setyaningsih" target="_blank">Reni Setyaningsih</a>
- [CC] C040DSX2415 - <a href="https://github.com/Iqbalalfarizi" title="GitHub Iqbal Alfarizi" target="_blank">Iqbal Alfarizi</a>
- [CC] C066DSX0786 - <a href="https://github.com/zflash123" title="GitHub Zaed Abdullah" target="_blank">Zaed Abdullah</a>
- [MD]	A066DSX1060 - <a href="https://github.com/oxychan" title="GitHub Taufik Anwar" target="_blank">Taufik Anwar</a>
