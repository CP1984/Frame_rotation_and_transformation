import numpy as np

class PointRotator:
    def __init__(self, theta_x_degrees, theta_y_degrees, theta_z_degrees):
        self.theta_x = np.radians(theta_x_degrees)  # Rotation along x-axis
        self.theta_y = np.radians(theta_y_degrees)  # Rotation along y-axis
        self.theta_z = np.radians(theta_z_degrees)  # Rotation along z-axis

        # Rotation matrices
        self.R_x = np.array([[1, 0, 0],
                             [0, np.cos(self.theta_x), -np.sin(self.theta_x)],
                             [0, np.sin(self.theta_x), np.cos(self.theta_x)]])
        
        self.R_y = np.array([[np.cos(self.theta_y), 0, np.sin(self.theta_y)],
                             [0, 1, 0],
                             [-np.sin(self.theta_y), 0, np.cos(self.theta_y)]])
        
        self.R_z = np.array([[np.cos(self.theta_z), -np.sin(self.theta_z), 0],
                             [np.sin(self.theta_z), np.cos(self.theta_z), 0],
                             [0, 0, 1]])

    def rotate_in_original_frame(self, rotate_1, rotate_2, rotate_3, original_point):
        """
        Applies a series of rotations to the original_point, along the axis in the original frame.

        Args:
            rotate_1 (numpy.ndarray): First rotation.
            rotate_2 (numpy.ndarray): Second rotation.
            rotate_3 (numpy.ndarray): Third rotation.
            original_point (numpy.ndarray): Point in the original frame.

        Returns:
            numpy.ndarray: Rotated point value in the original frame after applying all rotations.
        """
        rotated_point = np.dot(rotate_3, np.dot(rotate_2, np.dot(rotate_1, original_point)))
        return rotated_point

    def Euler_rotation(self, rotate_1, rotate_2, rotate_3, original_point):
        """
        Applies a series of rotations to the original_point by Euler rotation.

        Args:
            rotate_1 (numpy.ndarray): First rotation.
            rotate_2 (numpy.ndarray): Second rotation.
            rotate_3 (numpy.ndarray): Third rotation.
            original_point (numpy.ndarray): Point in the original frame.

        Returns:
            numpy.ndarray: Rotated point value in the original frame after applying all rotations.
        """
        rotated_point = np.dot(rotate_1, np.dot(rotate_2, np.dot(rotate_3, original_point)))
        return rotated_point

if __name__ == "__main__":
    original_x = 0.0
    original_y = 0.0
    original_z = 1.0

    rotate_x_degrees = 90
    rotate_y_degrees = 90
    rotate_z_degrees = 0
    original_point = np.array([original_x, original_y, original_z])
    rotator = PointRotator(rotate_x_degrees, rotate_y_degrees, rotate_z_degrees)

    print("Point value in original frame:{}, {}, {}".format(original_x, original_y, original_z))

    print("==========Rotate in original frame==========")
    rotated_point = rotator.rotate_in_original_frame(rotator.R_x, rotator.R_y, rotator.R_z, original_point)
    print(f"Original point: {original_point}")
    print(f"Rotated in original frame: {rotated_point}")

    print("==========Rotate in Euler==========")
    print(f"Original point: {original_point}")
    rotated_point = rotator.Euler_rotation(rotator.R_x, rotator.R_y, rotator.R_z, original_point)
    print(f"Euler rotation: {rotated_point}")