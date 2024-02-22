import utils.imports as imp
import utils.visuals as visu

# cargar dataset diabetes desde folder data
dataset = imp.read_diabetes_dataset("data/diabetes.tab.txt")


# Generar y guardar los histogramas para una exploración inicial
visu.save_histogram(dataset, "AGE")
visu.save_histograms(dataset)
<<<<<<< Updated upstream
=======
visu.save_correlation(dataset, "BMI","S6")
visu.save_all_correlations(dataset, dataset.corr())
>>>>>>> Stashed changes
