import numpy as np

class CoordinateConverter:
    def __init__(self):
        pass

    def convert_cartesian_to_spherical(self, x, y, z):
        # Calculate the radius (r)
        r = np.sqrt(x**2 + y**2 + z**2)
        
        # Calculate the polar angle theta (in degrees)
        theta_degrees = np.degrees(np.arccos(z / r))
        
        # Calculate the azimuthal angle phi (in degrees)
        phi_degrees = np.degrees(np.arctan2(y, x))
        
        return r, theta_degrees, phi_degrees

if __name__ == "__main__":
    # Test
    x = 1
    y = 1
    z = 1
    # [-0.09497707  0.0434222   0.99453198]-0.09488667  0.04361939  0.99453198]
    converter = CoordinateConverter()
    r, theta, phi = converter.convert_cartesian_to_spherical(x, y, z)
    print(f"Cartesian coordinates ({x}, {y}, {z}) correspond to spherical coordinates:")
    print(f"Radius r = {r}")
    print(f"Polar angle θ = {theta} degrees")
    print(f"Azimuthal angle φ = {phi} degrees")