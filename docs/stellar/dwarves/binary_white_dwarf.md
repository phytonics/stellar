# Binary White Dwarves

Previously, we have considered stars as isolated systems that evolve independently. However, most stars in the universe exist not as isolated stars, but as binaries, where two stars orbit their shared center of mass. When one of the stars in a binary system becomes a white dwarf, it forms what is known as a **Binary White Dwarf System**. 

## Recap: White Dwarves

A white dwarf is the remnant of a dead star -- only inert carbon that does not fuse remains, remaining light coming from only its remaining heat. Usually, a white dwarf will simply cool as it radiates its remaining heat, eventually forming a black dwarf. However, in a binary system, the white dwarf has the potential to evolve further -- and in far mmore spectacular ways.

## Stealing Gas

In a binary white dwarf system, the white dwarf's gravitational field can begin to pull gas from its partner to itself -- in other words, the size of its partner exceeds their Roche lobe, or the sphere of their gravitational influence. The result is that the white dwarf slowly gains gas from its partner. 

<p align="center">
    <img src="../../../assets/dwarves/mass_accretion.PNG"><br>Accretion of mass from a red giant</img>
</p>

This process, where the white dwarf gradually gains mass from its partner, is known as **accretion**.

## Accretion Disks

While the white dwarf attempts to pull mass from its partner straight towards itself, the spinning of the entire binary star system as well as the small size of the white dwarf makes it very easy for the mass to "miss" the white dwarf and go into orbit around it instead. A combination of tidal forces and the centripetal force from the gravitational pull stretches the gas into a thin, round layer surrounding the white dwarf, which is visible as an **accretion disk**.

<p align="center">
    <img src="../../../assets/dwarves/accretion_disk.jpg"><br>An accretion disk around a white dwarf</img>
</p>

As gas particles in the swirling disk collide, they will lose energy and be unable to sustain their existing orbital position, falling towards the white dwarf's surface. As the gas falls, it heats up -- so hot that it begins to radiate with peak wavelengths in visible and even ultraviolet and X-ray ranges, radiating light that outshines the white dwarf itself. 

## Gas Buildup, Novas and Supernovas

As the gas accumulates on the white dwarf surface, it becomes hotter and denser as the pressure too increases. At a critical point, the hydrogen ignites and begins to fuse into helium, forming a **nova**. In an even more extreme case, the white dwarf gains so much mass that its gravity can no longer be balanced by the repulsion from its degenerate electrons, and the entire white dwarf collapses on itself and explodes in a **Type Ia supernova**.

[Next: Novas](../nova/nova.md)  
[Next: Type Ia Supernovas](../nova/type_1a_supernova.md)

## Test Yourself!
### Question: Accretion

!!! Question "Which of the following is a white dwarf most likely to accrete gas from?"
	<div>
	<button class='md-button quizNormal' id="q1_1" onClick="markQ1(0)">White Dwarf</button>
	<button class='md-button quizNormal' id="q1_2" onClick="markQ1(1)">Red Giant</button>
    <button class='md-button quizNormal' id="q1_3" onClick="markQ1(2)">Neutron Star</button>
	<hr>
	</div>
??? Abstract "Solution and Explanation"
	_The gravitational influence of a star is dependent on its mass. White Dwarfs are empty husks, and have practically no mass to steal in the first place; while neutron stars are extremely dense and have very small volumes. In contrast, Red Giants have large volumes for their mass, and hence are likely to exceed their own gravitational influence, making it easier for a white dwarf binary to accrete gas._

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

https://www.nationalgeographic.com/science/article/white-dwarfs \
https://www.skyatnightmagazine.com/space-science/accretion-disk/ \
Astronomy Today
Images sourced from Astronomy Today and Science Photo Library
