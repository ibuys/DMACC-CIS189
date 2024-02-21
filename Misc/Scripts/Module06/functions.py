
"""
Functions to compute areas and volumes of different shapes.
"""
from math import pi



def get_triangle_area(b, h):
    """
    Compute area of triangle with base b and height h.

    Parameters
    ----------
    b: float
        Triangle base width.

    h: float
        Triangle height.

    Returns
    -------
    float 
        Area of triangle. 
    """
    area = .50 * b * h
    return area



def get_circle_area(r):
    """
    Compute area of circle with radius r.

    Parameters
    ----------
    r: float
        Circle radius.

    Returns
    -------
    float 
        Area of circle with radius r.    
    """
    area = pi * r**2
    return area



def get_sphere_volume(r):
    """
    Compute volume of sphere with radius r.

    Parameters
    ----------
    r: float
        Sphere radius.

    Returns
    -------
    float 
        Volume of sphere with radius r.    
    """
    volume = (4 / 3) * pi * r**3
    return volume
