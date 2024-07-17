# Rejuve on Galaxy

## To run this project
 
**Run the following commmands**

**create a virtual machine**
```bash 
virtualenv .venv; . venv/bin/activate
```

**Activate the virtual environment if it hasn't been already**
```bash 
source venv/bin/activate 
```

**Upgrade pip if needed.**
```bash 
pip install --upgrade pip
```

**Install planemo**

Planemo is a set of Command-line utilities to assist in developing Galaxy and Common Workflow Language artifacts - including tools, workflows, and training materials.
```bash 
pip install planemo 
```

**Afterwards to run the server run**
```bash
 planemo s 
 ```
 Or
 ```bash
 planemo serve 
 ```
Planemo will download and configure a disposable Galaxy instance before running the server if you want to avoid that, clone the following repository 

```bash
git clone https://github.com/galaxyproject/galaxy 
```

then run
```bash
 planemo s --galaxy_root="PATH_TO_GALAXY_REPO"
 ```
 Or
```bash
planemo serve --galaxy_root="PATH_TO_GALAXY_REPO"
```