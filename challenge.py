import math

def square_area(side):
    if side < 0:
        return False
    return side * side


def rectangle_area(base, height):
    return base * height

def triangle_area(base, height):
    return (base * height)/2

def rhombus_area(diagonal_1, diagonal_2):
    return diagonal_1 * diagonal_2

def trapezoid_area(base_minor, base_major, height):
    return ((base_minor+ base_major)/2) * height

def regular_polygon_area(perimeter, apothem):
    return (perimeter * apothem)/2

def circumference_area(radius):
    return math.pi * (radius**2)

if __name__ == '__main__':
    print()
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.squares = {
            # Orden de los datos
            # Resultado: Side
                0 : 0,
                1 : 1,
                4: 2,
                False : -1,
                9 : 3,
                16 : 4,
                25 : 5 ,
                36: 6 ,
                49 : 7,
            }

            self.rectangles =  {
            # Orden de los datos
            # Resultado : base , altura
                1 : [1,1],
                2 : [1,2],
                3 : [1,3],
                2 : [2,1],
                4 : [2,2],
                6 : [2,3],
                3 : [3,1],
                6 : [3,2],
                9 : [3,3],
            }

            self.triangles = {
            #Orden de los datos
            # Resultado: Base, altura
                0.5 : [1,1],
                1 : [1,2],
                1.5 : [1,3],
                1 : [2,1],
                2 : [2,2],
                3 : [2,3],
                1.5 : [3,1],
                3 : [3,2],
                4.5 : [3,3],
            }

            self.rhombus = {
            #Orden de los datos
            # Resultado: diagonal_1, diagonal_2
                1 : [1,1],
                2 : [1,2],
                3 : [1,3],
                2 : [2,1],
                4 : [2,2],
                6 : [2,3],
                3 : [3,1],
                6 : [3,2],
                9 : [3,3],
            }

            self.trapezoids = {
            #Orden de los datos
            # Resultado: base_menor, base_mayor, altura
                1 : [1,1,1],
                2 : [1,1,2],
                1.5 : [2,1,1],
                3 : [2,1,2],
                2 : [3,1,1],
                4 : [3,1,2],
                1.5 : [1,2,1],
                3 : [1,2,2],
                2 : [2,2,1],
                4 : [2,2,2],
                2.5 : [3,2,1],
                5 : [3,2,2],
            }

            self.regular_polygons = {
            #Orden de los datos
            # Resultado: perimetro, apothem
                0.5 : [1,1],
                1 : [1,2],
                1.5 : [1,3],
                1 : [2,1],
                2 : [2,2],
                3 : [2,3],
                1.5 : [3,1],
                3 : [3,2],
                4.5 : [3,3],
            }

            self.circunferences ={
            #Orden de los datos
            # Resultado: radio
                0 : 0,
                3.1416 : 1,
                12.5664: 2,
                28.2743 : 3,
                50.2655 : 4,
                78.5398 : 5 ,
                113.0973: 6 ,
                153.938 : 7,
                201.0619 : 8,

            }

        def test_square_area(self):
            for key, value in self.squares.items():
                self.assertEqual(key, square_area(value),)
        
        def test_rectangle_area(self):
            for key, value in self.rectangles.items():
                self.assertEqual(key, rectangle_area(value[0],value[1]))  
        
        def test_triangle_area(self):
            for key, value in self.triangles.items():
                self.assertEqual(key, triangle_area(value[0],value[1]))  

        def test_rhombus_area(self):
            for key, value in self.rhombus.items():
                self.assertEqual(key, rhombus_area(value[0],value[1]))  
        
        def test_trapezoid_area(self):
            for key, value in self.trapezoids.items():
                self.assertEqual(key, trapezoid_area(value[0],value[1],value[2])) 

        def test_regular_polygon_area(self):
            for key, value in self.regular_polygons.items():
                self.assertEqual(key, regular_polygon_area(value[0],value[1])) 

        def test_circumference_area(self):
            for key, value in self.circunferences.items():
                self.assertEqual(key, round(circumference_area(value),4)) 

        def tearDown(self):
            del(self.squares)
            del(self.rectangles) 
            del(self.triangles) 
            del(self.rhombus)
            del(self.trapezoids)
            del(self.regular_polygons)
            del(self.circunferences)


    unittest.main()
