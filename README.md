# Data-Engineering-First-Project: Data warehouse tech stack with MySQL, DBT, Airflow

## Project Description

This is a Data Engineering project created within 10 Academy Training! In this repository, we create a scalable data warehouse to handle and process the vehicle trajectory data collected by [pNEUMA experiment](https://open-traffic.epfl.ch/index.php/about/). The aim is to build a pipeline that facilitates the data use by the city traffic department to improve traffic flow and support various undisclosed projects.

### Data

pNEUMA is an open large-scale dataset of naturalistic trajectories of half a million vehicles that have been collected by a swarm of drones and static roadside cameras in the congested downtown area of Athens, Greece. 
- The vehicle trajectory data is extracted from analyzing traffic footage.  
- Each file for a single (area, date, time) is ~87 MB data.  


### Project Goals

- Create a scalable data warehouse (DWH) to host and manage vehicle trajectory data.
- Take into account future needs, organize the data such that downstream projects can query it efficiently. 
- Use the ELT framework using DBT (Data Build Tool). It is more suitable than ETL framework, because this way transformations can be set up on a need basis by analytic engineers.

## Tech Stack

We have chosen a robust tech stack to implement the data warehouse and support the ELT process efficiently. The main components of our tech stack include:

1. **PostgreSQL Database**: PostgreSQL will serve as the backbone of our data warehouse. It is a well-established relational database management system that can handle large-scale data efficiently and reliably.

2. **DBT (Data Build Tool)**: DBT will be the heart of our ELT framework. It enables us to transform the raw data into structured, queryable data models. The powerful templating and SQL-based workflow of DBT simplify the data transformation process and ensure maintainable code.

3. **Airflow**: Apache Airflow will be used to orchestrate the ELT workflows. It provides a powerful and flexible platform to schedule, monitor, and manage the data pipelines. With Airflow, we can automate the entire data processing pipeline and ensure smooth execution of tasks.

## Repository Structure

The repository is structured in the following manner:

- [/data](/data/): This directory contains sample data used for testing and development purposes.

- [/database](/database/): This directory holds scripts needed to setup the database, and create the tables.

- [/dbt](/dbt/): The directory houses all the DBT-related files and configurations. It includes models, and schema definitions.

- [/dags](/dags/): In this directory you find the Airflow DAG (Directed Acyclic Graph) files. These DAGs define the workflows for our data pipeline.

- [/scripts](/scripts/): This directory holds helper scripts that are needed for data preprocessing.

- [/screenshots](/screenshots/): This directory stores multiple screenshots of the data pipeline, including DAG runs from Airflow UI and model documentation from dbt UI. 

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local development environment.
    ```bash
    git clone https://github.com/emtinanseo/Traffic-Data-Warehousing.git
    ```

2. Set up the PostgreSQL and ensure it is accessible from your environment.

3. Set AIRFLOW_HOME to a local folder 
    ```bash
    export AIRFLOW_HOME=/absolute/path/to/folder/airflow
    ```
4. Install the required dependencies from [requirements.txt](/requirements.txt) file, including airflow and dbt
    ```bash
    cd Traffic-Data-Warehousing
    pip install -r requirements.txt
    ```
5. DBT Configuration: Configure DBT to connect to your PostgreSQL database by updating the necessary configurations in the `dbt/profiles.yml` file.

6. Airflow Configuration: in the AIRFLOW_HOME folder, set in step 3, open `airflow.cfg` file and change the value of `dags_folder` to
    ```
    # airflow.cfg
    dags_folder = /path/to/Traffic-Data-Warehousing/dags
    ```
7. Run the airflow pipelines
    * Initialize the database tables 
        ```bash
        airflow db init
        ```
    * Create a user
        ```bash
        airflow users create --username admin --firstname <firstname> --lastname <lastname> --role Admin --email <email>
        ```
    * Run the scheduler 
        ```bash
        airflow scheduler
        ```
    * [optional] Open airflow web UI
        ```bash
        airflow webserver --port 8080
        ```
        Then open the browser to http://localhost:8080/
    
## Contributing
We welcome contributions to enhance the data warehouse tech stack or improve the project's documentation. If you find any bugs or have suggestions for new features, please feel free to open an issue or submit a pull request.

## Authors
👤 **Emtinan Osman**
[Email](mailto:emtinan.s.e.osman@gmail.com), [GitHub](https://github.com/emtinanseo), [LinkedIn](https://www.linkedin.com/in/emtinan-elkhidir-osman-646242119/)