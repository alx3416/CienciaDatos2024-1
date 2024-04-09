import utils.imports as imp
import utils.visuals as visu
import utils.processing as proc

# cargar dataset diabetes desde folder data
dataset = imp.read_diabetes_dataset("data/diabetes.tab.txt")

# Generar y guardar los histogramas para una exploración inicial
# visu.save_histogram(dataset, "AGE")
# visu.save_histograms(dataset)
# visu.save_correlation(dataset, "BMI", "S6")
# visu.save_all_correlations(dataset, dataset.corr())
# visu.save_all_correlations_one_image(dataset)

norm_dataset = proc.normalize_diabetes_data(dataset)
training_data, test_data = proc.split_data(dataset, 0.7)
training_input = training_data[['AGE', 'SEX', 'BMI']]
training_output = training_data["Y"]
model = proc.regression_tree(training_input, training_output, 3)

test_input = training_data[['AGE', 'SEX', 'BMI']]
test_output = training_data["Y"]
test_predictions = proc.test_predictions(model, test_input, 3)

visu.plot_model_tree(model, ['AGE', 'SEX', 'BMI'])
MSE = proc.get_mean_squared_error(test_output,
                                  test_predictions)
print("Mean Squared Error: ", MSE)
R2 = proc.get_coefficient_determination(test_output,
                                        test_predictions)
print("R² Score: ", R2)
