import tensorflow as tf
from openpyxl import load_workbook

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

def create_NN(name, hidden_layers, neurons_per_hl):
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    
    while hidden_layers > 0:
        model.add(tf.keras.layers.Dense(neurons_per_hl, activation='relu'))
        hidden_layers -= 1

    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)

    test_loss, test_accuracy = model.evaluate(x_test, y_test)
    
    print(test_loss)
    print(test_accuracy)
        
    wb = load_workbook('results.xlsx')
    file = wb.active

    file.append([name, test_accuracy, test_loss])


    wb.save(filename='results.xlsx')

def generator(name, neurons_per_hl):
    hidden_layers = 1
    
    while hidden_layers <= 5:
        name_and_number = name + " with " + str(hidden_layers) + " layers"
        create_NN(name_and_number, hidden_layers, neurons_per_hl)
        hidden_layers += 1

# generator('Mean of Input and Output Neurons', 397)
# generator('Input Layer Neurons', 784)
# generator('Output Layer Neurons', 10)
# generator('Half of Input Neurons', 392)
# generator('Quarter of Input Neurons', 196)
# generator('Two Times Input Neurons', 1568)
# generator('100 Neurons', 100)
# generator('200 Neurons', 200)
# generator('300 Neurons', 300)
# generator('400 Neurons', 400)
# generator('500 Neurons', 500)
# generator('1000 Neurons', 1000)
# generator('Five Times Input Neurons', 3920)
# generator('Ten Times Input Neurons', 7840)
# generator('20% Input Neurons', 157)
# generator('10% Input Neurons', 78)
# create_NN('No Hidden Layer', 0, 0)
# generator('One Nueron Per Layer', 1)
generator('2 Neurons per Layer', 2)
generator('3 Neurons per Layer', 3)
generator('4 Neurons per Layer', 4)
generator('5 Neurons per Layer', 5)
# generator('10 Neurons Per Layer', 10)