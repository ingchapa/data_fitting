import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

class Analyst:
    """A class to analyze the data"""

    def fit_norm_dists(self, variable, batch, save_path):
        """Fit the norm and lognorm statistical distributions to the data"""
        dict_names = ['shape', 'loc', 'scale', 'mean', 'median', 'mode', 'std', 'variance', 'cv']
        #Get the data-----------------------------------------------------------
        data = variable.batches[batch]
        #Define the spacing for the model
        x = np.linspace(data.min(), data.max(), 100)
        #Fit the NORMAL distributions and compute the statistics----------------
        norm_fit = self.create_empty_dict(names=dict_names, prefix='norm_')
        norm_fit['norm_loc'], norm_fit['norm_scale'] = scipy.stats.distributions.norm.fit(data)
        norm_fit['norm_shape'] = 0
        norm_fit['norm_mean'] = norm_fit['norm_loc']
        norm_fit['norm_median'] = norm_fit['norm_loc']
        norm_fit['norm_mode'] = norm_fit['norm_loc']
        norm_fit['norm_std'] = norm_fit['norm_scale']
        norm_fit['norm_variance'] = norm_fit['norm_std']**2
        norm_fit['norm_cv'] = norm_fit['norm_std']/norm_fit['norm_mean']*100
        norm_x = scipy.stats.distributions.norm.pdf(x, norm_fit['norm_loc'], norm_fit['norm_scale'])
        #Fit the LOGNORMAL distributions and compute the statistics-------------
        lognorm_fit = self.create_empty_dict(names=dict_names, prefix='lognorm_')
        lognorm_fit['lognorm_shape'], lognorm_fit['lognorm_loc'], lognorm_fit['lognorm_scale'] = scipy.stats.distributions.lognorm.fit(data, floc=0)
        lognorm_fit['lognorm_median'] = lognorm_fit['lognorm_scale']
        lognorm_fit['lognorm_std'] = lognorm_fit['lognorm_shape']
        lognorm_fit['lognorm_mean'] = lognorm_fit['lognorm_scale']*np.exp(0.5*lognorm_fit['lognorm_std']**2)
        lognorm_fit['lognorm_mode'] = lognorm_fit['lognorm_scale']*np.exp(-lognorm_fit['lognorm_std']**2)
        lognorm_fit['lognorm_variance'] = (np.exp(lognorm_fit['lognorm_std']**2)-1)*lognorm_fit['lognorm_mean']**2
        lognorm_fit['lognorm_cv'] =(np.exp(lognorm_fit['lognorm_std']**2)-1)**(0.5)*100
        lognorm_x = scipy.stats.distributions.lognorm.pdf(x, lognorm_fit['lognorm_shape'], lognorm_fit['lognorm_loc'], lognorm_fit['lognorm_scale'])
        #Compute the statistics from the DATA-----------------------------------
        data_fit = self.create_empty_dict(names=dict_names, prefix='data_')
        data_mean = data.mean()
        data_cv = data.std()/data.mean()
        data_std = data_cv*data.mean()
        data_fit['data_scale'] = data_mean**2/((data_mean**2 + data_std**2)**(1/2))
        data_fit['data_std'] = (np.log(1+data_cv**2))**(1/2)
        data_fit['data_shape'] = data_fit['data_std']
        data_fit['data_loc'] = 0
        data_fit['data_median'] = data_fit['data_scale']
        data_fit['data_mean'] = data_fit['data_scale']*np.exp(0.5*data_fit['data_std']**2)
        data_fit['data_mode'] = data_fit['data_scale']*np.exp(-data_fit['data_std']**2)
        data_fit['data_variance'] = (np.exp(data_fit['data_std']**2)-1)*data_fit['data_mean']**2
        data_fit['data_cv'] =(np.exp(data_fit['data_std']**2)-1)**(0.5)*100
        data_x = scipy.stats.distributions.lognorm.pdf(x, data_fit['data_shape'], data_fit['data_loc'], data_fit['data_scale'])
        #Plot-------------------------------------------------------------------
        plt.hist(data, density=True, bins=20, alpha=0.7, label='data', color='limegreen')
        plt.plot(x,norm_x,'k-', label='normal')
        plt.plot(x,lognorm_x,'r-', label='lognormal')
        plt.plot(x,data_x,'r--', label='data-based lognormal')
        plt.title(batch)
        plt.xlabel(variable.name + ' (%)', fontsize=12)
        plt.ylabel('Probability (%)', fontsize=12)
        plt.legend()
        save_name = save_path + variable.name + '_' + batch + '.png'
        plt.savefig(save_name)
        plt.close('all')
        return norm_fit, lognorm_fit, data_fit

    def create_empty_dict(self, names, prefix):
        """Create an empty dictionary from the names"""
        empty_dict = {}
        for name in names:
            name = prefix + name
            empty_dict[name] = None
        return empty_dict
