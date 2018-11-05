# data_python

## Install requirements :
	pip install -r requirements.txt
	

### Qu'est-ce qu'un module ?

Un module est un fichier contenant des instructions écrites en Python. Le nom du fichier est le nom du module. Par exemple, le fichier csv_analysis.py devient le module csv_analysis.

### Qu'est-ce qu'une librairie (paquet = package) ?

Un ensemble de modules.

Cette organisation vous permet de les importer en utilisant une autre syntaxe en "point nomdumodule". Par exemple, un module qui s'appelle A.B désigne un sous-module appelé B dans un paquet s'appelant A.

Un paquet contient impérativement un fichier ``` __init__.py ```par module(ici notre module *analysis* ). Un dossier sans ce fichier ne sera pas reconnu comme étant un module du paquet. et en plus notre libraie(paquet) contient impérativement un fichier ```setup.py```

rappel de l'organisation de notre librairie:
- analysis
   - ```__init__.py```
   - csv.py
   - xml.py
- data
   - current_mps.csv
   - SyceronGlobal.xml
- parite.py
- setup.py

La librairie standard **Argparse**  contient de nombreuses méthodes très utiles pour récupérer des arguments.
- Nous allons l'utiliser en trois temps :
	- Création d'un objet ArgumentParser()
	- Lecture des arguments
	- Renvoi des arguments
	
Exécutez la commande :
	
	$ python parite.py -e csv
ou :
	
	$ python parite.py --extension csv

### Installer les trois librairies:
 **Matplotlib**, c'est pour les graphiques. 
	
		pip install matplotlib
		
 **Numpy**, c'est pour manipuler des données, et plus précisément des séries de nombres.
		
		pip install numpy
		
**Pandas** introduit un objet très pratique appelé le Dataframe.

		pip install pandas

install also:
	
	sudo apt-get install python3-tk

	pip3 install seaborn


console test example:

	python3 parite.py -e csv -d current_mps.csv -p
