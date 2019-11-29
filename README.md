# simba-scrapy-chelonia-mydas
A web scrapy of Chelonia mydas (Green Turtle) to get images of the animals from https://segurogis.petrobras.com.br.

This project can download images from turtles (Chelonia mydas) from Segurogis SIMBA, based on a xlsx file (check Ocorrências de fauna alvo individual 12_02_2019 20_01.xlsx). You may get this in the filters page.

You can use the "Ocorrências de Fauna Individual" or "Ocorrências de Fauna Alvo Coletiva"
Example of filter list: https://segurogis.petrobras.com.br/simba/web/sistema/pmp/1/individualfaunaoccurrence/
You can use the filters to specify the specie chelonia mydas.
The example file in this repository get's chelonia mydas from a range of time.

To work with it we recommend you to use an environment:
conda create --name myenv
conda activate myenv

Install the dependencies from requirements.txt file
conda install --yes --file requirements.txt

Install scrapy
conda install -c conda-forge scrapy

If you want to skip install, you may import the env from environment.yml

You may configure the output folder in BASE_OS_TURTLE_PATH const located at scrappy.py.

To run the project execute
scrapy runspider scrappy.py
