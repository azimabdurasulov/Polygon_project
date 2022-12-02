from math import pi
class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        return self.radius>0 and self.radius!=0 
    
    def diameter(self):
        '''
        This method finds the diameter of the circle.

        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        return 
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.

        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid:
            return self.radius*2*pi
        return False
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.

        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        if self.is_valid:
            return self.radius*self.radius*pi
        return False 