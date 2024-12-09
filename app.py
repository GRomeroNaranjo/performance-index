from sklearn.preprocessing import MinMaxScaler
import math
import numpy as np

class CalculateValues():
    def __init__(self):
        pass
    
    def calculate_s(self, time_1, time_2, time_3, time_4, time_5):
        
        distance_1 = 1.5 - time_1
        distance_2 = 1.5 - time_2
        distance_3 = 1.5 - time_3
        distance_4 = 1.5 - time_4
        distance_5 = 1.5 - time_5

        t_1 = abs(distance_1)
        t_2 = abs(distance_2)
        t_3 = abs(distance_3)
        t_4 = abs(distance_4)
        t_5 = abs(distance_5)

        s = math.mean([t_1, t_2, t_3, t_4, t_5])
        return s

    def calculate_c(self, x_1, x_2, x_3, x_4, x_5):
        c = math.mean([x_1, x_2, x_3, x_4, x_5])
        return c
    
    def calculate_a(self, x_1, x_2, x_3, y_1, y_2, y_3, z_1, z_2, z_3, a_1, a_2, a_3, b_1, b_2, b_3):
        x = math.mean([x_1, x_2, x_3])
        y = math.mean([y_1, y_2, y_3])
        z = math.mean([z_1, z_2, z_3])
        a = math.mean([a_1, a_2, a_3])
        b = math.mean([b_1, b_2, b_3])

        final_a = math.mean([x, y, z, a, b])
        return final_a
    

class FinalValues():
    def __init__(self):
        self.calculate = CalculateValues()
        self.scaler = MinMaxScaler()

    def calculate_s(self):
        time_1 = input("Enter the time value 1:")
        time_2 = input("Enter the time value 2:")
        time_3 = input("Enter the time value 3:")
        time_4 = input("Enter the time value 4:")
        time_5 = input("Enter the time value 5:")

        time = self.calculate.calculate_s(time_1, time_2, time_3, time_4, time_5)
        return time

    def calculate_c(self):
        x_1 = input("Enter the x value 1:")
        x_2 = input("Enter the x value 2:")
        x_3 = input("Enter the x value 3:")
        x_4 = input("Enter the x value 4:")
        x_5 = input("Enter the x value 5:")

        c = self.calculate.calculate_c(x_1, x_2, x_3, x_4, x_5)
        return c
    
    def calculate_a(self):
        x_1 = input("Enter the x value 1:")
        x_2 = input("Enter the x value 2:")
        x_3 = input("Enter the x value 3:")
        y_1 = input("Enter the y value 1:")
        y_2 = input("Enter the y value 2:")
        y_3 = input("Enter the y value 3:")
        z_1 = input("Enter the z value 1:")
        z_2 = input("Enter the z value 2:")
        z_3 = input("Enter the z value 3:")
        a_1 = input("Enter the a value 1:")
        a_2 = input("Enter the a value 2:")
        a_3 = input("Enter the a value 3:")
        b_1 = input("Enter the b value 1:")
        b_2 = input("Enter the b value 2:")
        b_3 = input("Enter the b value 3:")

        a = self.calculate.calculate_a(x_1, x_2, x_3, y_1, y_2, y_3, z_1, z_2, z_3, a_1, a_2, a_3, b_1, b_2, b_3)
        return a

    def calculate_metric(self):
        s = self.calculate_s()
        c = self.calculate_c()
        a = self.calculate_a()

        self.scale.fit([[s, c, a]])
        s, c, a = self.scale.transform([[s, c, a]])

        index = (a + c + a) / 3
        return index


def main():
    final = FinalValues()
    index = final.calculate_metric()
    print("The final index value is:", index)

    


    


      



