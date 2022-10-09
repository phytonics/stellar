# Type Ia Supernova
<p align="center">
    <img src="../../../assets/nova/supernova.png"><br>A visible supernova</img>
</p>

White dwarves in binary systems slowly accrete mass from their partners, and can eventually turn into [novas](nova.md) or **Type Ia Supernovas**. Supernovas obtain their name as they flare up suddenly like novas, but have even greater brightness than them as their name would suggest. Despite their similar names oweing to the similar phenomenon at the surface level, the mechanisms behind supernovas actually are quite distinct from that of novas. 

## Supernovas vs Novas

Unlike the recurring novas, supernovas explode only once. The reason for supernovas occuring only once is a direct result of the greater magnitude of their burst of brightness, since this greater energy release destroys the whole star.

## Types of Supernova

Supernovas today are divided into two types, Type I and Type II, based on how much hydrogen they contain, deduced from the emission lines of their radiation. Type I supernovas are characterized by being hydrogen-poor, and have brightness curves more similar to those of novas.

This article focuses specifically on Type Ia Supernovas: hydrogen-poor supernovas that arise from **[Binary White Dwarf Systems](../dwarves/binary_white_dwarf.md)**.

## Mass Accretion and Accumulation
Recall that in a binary white dwarf system, the white dwarf can accrete mass from its partner. When too much gas accumulates and pressure increases, the gas will tend to ignite in the form of a **nova**; however some gas still remains after the nova explosion. This remaining gas builds up over time, causing the mass of the white dwarf to increase.

## Balancing Pressures

Opposing the gravity of the white dwarf trying to collapse in on itself is the **electron degeneracy pressure**. In simple terms, the electrons cannot be squeezed any closer, and exert an outward pressure to resist further collapse. However, once gravity gets too strong from too much mass, it can overcome this pressure. 

The mass at which this occurs is calculated to be about 1.4 solar masses, which is known as the **Chandrasekhar mass** or **Chandrasekhar limit**. 

## The White Dwarf Collapses

The collapsing white dwarf causes its core to be forced together again, increasing the core's density and hence the intensity of gravity. Pressures become high enough for the carbon core of the white dwarf to undergo **carbon fusion**, which is the same process of that in massive stars. Carbon fusion can yield multiple products, for example in the following:

$$
\ce{^{12}_{6}C} + \ce{^{12}_{6}C} \rightarrow \ce{^{20}_{10}Ne} + \ce{^{4}_{2}He}
\ce{^{12}_{6}C} + \ce{^{12}_{6}C} \rightarrow \ce{^{23}_{11}Na} + \ce{^{1}_{1}H}
\ce{^{12}_{6}C} + \ce{^{12}_{6}C} \rightarrow \ce{^{23}_{12}Mg} + \ce{^{1}_{0}n}
$$

This process generates a huge amount of energy as practically the whole star undergoes fusion at once. This burst of energy overcomes the gravitational pull of the white dwarf's matter, and the white dwarf explodes and releases a large amount of light, which we observe as a **Type Ia Supernova**.

## After the Explosion
The white dwarf is obliterated in the supernova explosion, with its mass being thrown out into space by the force of the thermonuclear expansion and forming a supernova remnant.

[Next: Supernova Remnant](supernova_remnant.md)

## Test Yourself!
### Question: Supernova Factors

!!! Question "Which of the following is not a condition leading to a Type Ia Supernova?"
	<div>
	<button class='md-button quizNormal' id="q1_1" onClick="markQ1(0)">The pressure balance in a white dwarf being disrupted</button>
	<button class='md-button quizNormal' id="q1_2" onClick="markQ1(1)">The white dwarf gaining heat from its partner through radiation</button>
    <button class='md-button quizNormal' id="q1_3" onClick="markQ1(2)">A large partner star</button>
	<hr>
	</div>
??? Abstract "Solution and Explanation"
	_A large partner star is required for a white dwarf to accrete the mass it needs. This mass increases the gravity of the white dwarf until it overcomes the electron degeneracy and causes an imbalance in the pressures, leading to the collapse, and subsequent fusion of the carbon white dwarf. While the fusion does indeed occur partially due to the heating of the white dwarf as pressures increase, this is not related to the absorption of radiation from its partner, as the power gained from the process is extremely low._

<script>
function markQ1(answer) {
	const wrong1 = document.getElementById("q1_1")
    const wrong2 = document.getElementById("q1_3")
	const right = document.getElementById("q1_2")
	wrong1.classList.add("quizIncorrect")
    wrong2.classList.add("quizIncorrect")
	right.classList.add("quizCorrect")
}
</script>

*References:*

http://www.differencebetween.net/science/nature/differences-between-a-nova-and-a-supernova/
https://www.physics.rutgers.edu/analyze/wiki/Ia_supernovae.html (information and graph)
https://www.schoolsobservatory.org/learn/astro/stars/cycle/ia_supernova