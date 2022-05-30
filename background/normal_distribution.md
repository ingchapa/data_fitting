---
title: 'Estimation of log-normal distribution from data'
mainfont: Arial
papersize: 'a4'
pagestyle: 'plain'
geometry: 'left=2cm,right=2cm,top=3cm,bottom=3cm'
---
* Assume a known value for the mean ($\mu_x$) of the sample and the coefficient of variation ($cv$). Use VALE values and the CV obtained by data conciliation

* Assume that the coefficient of variation of the random variable $x$ is constant after the transformation into a random variable with a log-normal distribution $w=\ln (x)$. So, $cv_x = cv_w$

* Estimate the mean from the data or assume VALE mean as the arithmetic mean for the batch

$$
\mu_x = \frac{1}{n} \sum_{i=1}^n x_i
$$

* Estimate the standard deviation from the coefficient of variation of the data or assume a known cv for the batch

$$
\sigma_x = cv_x \cdot \mu_x
$$

* Estimate the mean of the log-normal distribution by using the equation:

$$
\exp{({\mu_w})} = \frac{\mu_x^2}{\sqrt{\mu_x^2 + \sigma_x^2}}
$$

* Estimate the standard deviation of the log-normal distribution by using the equation:
  
  $$
  cv_w = \sqrt{\exp(\sigma_w^2) - 1} \rightarrow \sigma_w = \sqrt{\ln(1+cv^2)}
  $$

* Compute the distribution:
  
  $$
  f(x) = \frac{\exp\left[-\frac{1}{2} \left(\frac{\ln x-\mu_w}{\sigma_w} \right)^2 \right]}{x \sigma_w \sqrt{2 \pi}}
  $$

* Compute the other statistics as:
  
  * mean $=\exp(\mu_w + \frac{1}{2} \sigma_w^2)$
  
  * median $= \exp(\mu_w)$
  
  * mode $=\exp(\mu_w - \sigma_w^2)$
  
  * variance $= \left[\exp(\sigma_w^2) -1 \right]\cdot \exp(2\mu_w + \sigma_w^2)$




