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
visu.save_all_correlations_one_image(dataset)

norm_dataset = proc.normalize_diabetes_data(dataset)
training_data, test_data = proc.split_data(norm_dataset, 0.7)
training_input = training_data[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']]
training_output = training_data["Y"]
model = proc.simple_linear_regression(training_input, training_output, 10)

test_input = training_data[['AGE', 'SEX', 'BMI', 'BP', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']]
test_output = training_data["Y"]
test_predictions = proc.test_predictions(model, test_input, 10)

coefficients = proc.get_coefficients(model)
print("Coefficients: ", coefficients)
MSE = proc.get_mean_squared_error(test_output,
                                  test_predictions)
print("Mean Squared Error: ", MSE)
R2 = proc.get_coefficient_determination(test_output,
                                        test_predictions)
print("R² Score: ", R2)

# Usemos columna SEX como variable categórica (logistic regression)
training_data, test_data = proc.split_data(norm_dataset, 0.7)
training_input = training_data[['AGE', 'BMI']]
training_output = training_data["SEX"]
test_input = test_data[['AGE', 'BMI']]
test_output = test_data["SEX"]
# salida debe ser categorical

# crear y entrenar modelo
model = proc.simple_linear_regression(training_input,
                                      training_output)
# predicciones con conjunto test

# Obtener matriz de confusión y medidas de calidad
names = ['male', 'female']