# Magnitude Scale

This is a brief overview of the Magnitude Scale system before we move on to the classification of stars.

The understand the Magnitude System, we must first start by discussing the historical significance of the system.

## Hipparchus and the Greek Observation

![Hipparchus (https://prabook.com/web/hipparchus.of_nicaea/3779216)](../../assets/preliminaries/hipparchus.jpg){ width="150", align=right }

Hipparchus of Nicea (190 BC - 120 BC) was one of the many astronomers in the time of the Greeks, and influenced much of what we understand of astronomy today. What sets him apart is he is still considered, to this date, the greatest astronomical observer in history. His work on star catalogs, spherical trigonometry and more still astounds astronomers working today, but what we want to focus on today is his work on the Magnitude Scale.

Prior to Hipparchus, most Greek astronomers believed that a star's brightness is only based on its size, which we now know is in fact false. There are many factors in play here, and we needed to spend more time analysing it.

Then Hipparchus himself came to the scene. As perhaps the greatest anicient astronomer, he used his ingenuity to group stars up into specific classes based on their perceived brightness. He assigned discrete integer values to each star, such that the brightest stars would fall into the _"Stars of the First Magnitude"_ and the barely visible stars were allocated to the _"Stars of the Sixth Magnitude"_.

The problem with this system was unfortunately the fact that just plain observation is incredibly subjective, since stars often vary in brightness. However, this set the seedling for what was yet to come...

## Norman Pogson

![Norman Pogson (https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/NR_Pogson.jpg/440px-NR_Pogson.jpg)](../../assets/preliminaries/pogson.jpg){ width="150", align=right }

In 1856, an Astronomer working at Oxford University by the name of Norman Pogson came up with an efficient scale to work with the preset definitions from Hipparchus.

He believed that our observation and hence tabulation of the magnitudes of different stars was influenced by a Logarithmic Scale. However, it wasn't purely based on a logarithmic scale in the conventional sense. Scaling and done to ensure that a simple step-down of 5 steps of magnitude would entail the star being about a **hundred** times brighter. To visualise, it would be something like this:

$$
\frac{F}{F_\text{ref}} = 100^{(m - m_\text{ref})/5}
$$

Where we have that $F$ and $m$ are the brightness (as intensity) and magnitude (as a decimal value). We have to base it off the referential object, reprsented by the $\text{ref}$ keyword.

## Reference Points

For the most part, astronomers used to use Polaris (the North Star) as a reference, defining its magnitude as about $+2.0$. However, it was later found that Polaris was a variable star, which essentially means that its brightness would vary with time.

We eventually moved to Vega, another star whose brightness was believed to be about $+0.0$