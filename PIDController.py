
class PIDController():

    def __init__(self, kp, ki, kd):
        self.error = 0
        self.errorPrevious = 0

        self.eP = 0
        self.eI = 0
        self.eD = 0

        self.kP = kp
        self.kI = ki
        self.kD = kd

        self.u = 0

    def update(self, error, deltaT):
        self.errorPrevious = self.error
        self.error = error

        self.eP = self.error
        self.eI = self.eI + self.error
        self.eD = self.error - self.errorPrevious

        self.u = self.eP*self.kP + self.eI*self.kI + self.eD*self.kD

        return self

    def get_u(self):

        return self.u