import numpy as np
class Policy:
    
    def __init__(self, cov):
        print('Running constructor ...')
        self.cov = cov
        self.policy_parameters = np.random.randint(100,size=(4))
        self.policy_parameters = self.policy_parameters.reshape((-1,1))
        self.mean_shift_array = np.array([])
        for i in range(4):
            mean_shift = np.random.rand(9)
            mean_shift[-1] *= np.random.uniform(-1.5, 1.5)
            mean_shift = mean_shift.reshape((-1,1))
            self.mean_shift_array = np.append(self.mean_shift_array, mean_shift)
        

    def phi_i(self, x, cov, mean, mean_shift=None):
        if(mean_shift==None):          # for original mean
            mean_shift = np.zeros(9)
        mean+=mean_shift
        self.mean = mean
        self.cov = cov
        m = mean.reshape((-1,1))
        x = x.reshape((-1,1))
        val = np.matmul((x-m).T, np.matmul(cov, (x-m)))
        phi_i_val = np.exp(-0.5*val.item())
        return phi_i_val
    
    def phi(self,s,a):
        s_a = np.append(s,a)
        phi_vec = np.array([])
        for i in range(4):
            phi_vec = np.append(
                self.phi_i(s_a, self.cov, self.mean, self.mean_shift_array[i]))
        return phi_vec

    def f_of_a_st(self, action, state):
        self.ACTIONS = np.array([0,1,2,3])
        self.exp_phi_theta = np.array([])
        for each_action in self.ACTIONS:
            val = np.matmul(self.phi(state,each_action).T, self.policy_parameters)
            self.exp_phi_theta = np.append(self.exp_phi_theta, val.item())
        result = self.exp_phi_theta[action]
        result /= sum(self.exp_phi_theta)
        return result

    def df_of_a_st(self, action, state):
        n1 = self.exp_phi_theta[action]*sum(self.exp_phi_theta)*self.phi(state, action)
        n2 = 0
        for each_action in self.ACTIONS:
            n2+=(self.exp_phi_theta[each_action]*self.phi(state, each_action))
        N = n1-n2
        D = sum(self.exp_phi_theta)**2
        result = N/D
        return result
    
    def dlogF_with_dPolicyParam(self, action, state):
        N = self.df_of_a_st(state, action)
        D = self.f_of_a_st(state, action)
        result = N/D
        return result


