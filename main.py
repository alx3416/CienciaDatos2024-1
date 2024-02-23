import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc

# cargar dataset diabetes desde folder data
dataset = imp.read_diabetes_dataset("data/diabetes.tab.txt")

# Generar y guardar los histogramas para una exploración inicial
visu.save_histogram(dataset, "AGE")
visu.save_histograms(dataset)
visu.save_correlation(dataset, "BMI", "S6")
visu.save_all_correlations(dataset, dataset.corr())

norm_dataset = proc.normalize_diabetes_data(dataset)
training_data, test_data = proc.split_data(norm_dataset, 0.7)
training_input = training_data[["BMI", 'AGE', 'S6']]
training_output = training_data["Y"]
model = proc.simple_linear_regression(training_input, training_output, 3)
print("ok")
