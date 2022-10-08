# Stellar Structure

The stellar structure is largely predicated by two distinct but important phenomena: **nuclear fusion** and **hydrostatic equilibrium**.

## Hydrostatic Equilibrium

<div align="center">
    <canvas id="myCanvas" width="500" height="465"></canvas>
    <div id="buttons">
    <button class='md-button quizNormal' id="play" onClick="play()">Play</button>
    <button class='md-button quizNormal' id="pause" onClick="pause()">Pause</button>
    <button class='md-button quizNormal' id="reset" onClick="reset()">Reset</button>
    </div>
<br>
     <div id="tempSlider">
      Temperature: Cold <input type="range" id="tempValue" min="0.6"
      max="3.4" value="1" step="0.05" oninput="changeTemp(this.value)" onchange="changeTemp(this.value)"> Hot &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
    </div>

    <p>
    Figure 1.2.1 - An Idealised Simulation of the Sun
    </p>


</div>

<script>
var canvas = document.getElementById("myCanvas");
var context = canvas.getContext("2d");
var simTitle = 'An Idealised Version of the Sun';

var time = 0.0;
var timer;
var runFlag = 1;
var numBalls = 200;
var diameter = 400;
var centerX = canvas.width/2;
var centerY = 235;
var ballRadius = 5;

var ball = new Array(numBalls);
for (var i = 0; i <= numBalls; i++) {
ball[i] = {};
ball[i].xValue = centerX;
ball[i].yValue = centerY;
ball[i].deltaX = -1.0+2.0*Math.random();
ball[i].deltaY = -1.0+2.0*Math.random();
ball[i].radius = ballRadius;
ball[i].color = "#242635";
}

var speedFactor = 1;
var overlap = create2DArray(numBalls,numBalls,0);
var oldOverlap = create2DArray(numBalls,numBalls,1);

runMotion();

function fill1DArray(length, init) {
    var x = new Array(length);
    for (var j = 0; j < length; j++) x[j] = init;
    return x;
}

function create2DArray(rows, columns, init) {
    var x = new Array(rows);
    for (var i = 0; i < rows; i++) x[i] = fill1DArray(columns, init)
    return x;
}

function drawMotion() {
    if (time >= 50) runFlag = 0;

    if (runFlag == 1) {
        context.clearRect(0, 0, canvas.width, canvas.height);
        
        context.fillStyle = "#242635";
        context.fillRect(0, 0, canvas.width, canvas.height);
        
        context.beginPath()
        context.arc(centerX, centerY, 0.5*diameter, 0, 2*Math.PI, false)
        context.fillStyle = "#F4C70A";
        context.fill()

        for (var i = 0; i<(numBalls-1); i++) {
            for (var j = i+1; j<numBalls; j++) {
                xDiff = ball[j].xValue-ball[i].xValue
                yDiff = ball[j].yValue-ball[i].yValue
                overlap[i][j] = ((xDiff*xDiff+yDiff*yDiff) < (2*ball[j].radius*2*ball[i].radius))*1;
                if ((overlap[i][j] == 1) && (oldOverlap[i][j] == 0)) {
                    vxi = ball[i].deltaX;
                    vyi = ball[i].deltaY;
                    
                    vxj = ball[j].deltaX;
                    vyj = ball[j].deltaY;

                    distance = Math.sqrt(xDiff*xDiff+yDiff*yDiff);
                    cosTheta = yDiff/distance;
                    sinTheta = xDiff/distance;

                    ball[i].deltaX = vxi + sinTheta*( -vxi*sinTheta + vxj*sinTheta - vyi*cosTheta + vyj*cosTheta);
                    ball[j].deltaX = vxj + vxi - ball[i].deltaX;
                    ball[i].deltaY = vyi + cosTheta*( -vyi*cosTheta + vyj*cosTheta - vxi*sinTheta + vxj*sinTheta);
                    ball[j].deltaY = vyj + vyi - ball[i].deltaY;
                }
                oldOverlap[i][j] = overlap[i][j];

            }
            
            ball[i].xValue = ball[i].xValue + speedFactor*ball[i].deltaX;
            ball[i].yValue = ball[i].yValue + speedFactor*ball[i].deltaY;

            let x = ball[i].xValue - centerX
            let y = ball[i].yValue - centerY

            let mag = Math.sqrt(x * x + y * y) + ball[i].radius

            if(mag > diameter*0.5) {
                console.log(`${ball[i].xValue} + ${ball[i].yValue} while ${diameter}`)
                uX = ball[i].deltaX
                uY = ball[i].deltaY
                uMag = Math.sqrt(uX*uX + uY*uY)

                pX = x
                pY = y
                pMag = Math.sqrt(pX*pX + pY*pY)
                phatX = pX/pMag
                phatY = pY/pMag

                proj = uX * phatX + uY * phatY
                projX = 2 * (uX - phatX * proj)
                projY = 2 * (uY - phatY * proj)

                dx = projX - uX
                dy = projY - uY
                if(Math.sqrt((x + dx)*(x+dx)+(y+dy)*(y+dy)) + ball[i].radius > diameter*0.5) {
                    ball[i].deltaX = -phatX * uMag
                    ball[i].deltaY = -phatY * uMag
                } else {
                    ball[i].deltaX = projX - uX
                    ball[i].deltaY = projY - uY
                }
                
            }

            context.fillStyle = ball[i].color;
            context.beginPath();
            context.arc(ball[i].xValue, ball[i].yValue, ball[i].radius, 0, 2 * Math.PI, false);
            context.fill();
        }

        context.font = 'bold 16pt Roboto';
        context.fillStyle = '#F4C70A';
        context.textAlign = 'center';
        context.fillText(simTitle, (canvas.width)/2, 25);
    }
}

function runMotion() {
    drawMotion();
    if (runFlag == 1) timer = window.setTimeout(runMotion, 20/60);
}
function changeTemp(newTempValue) {
    speedFactor = Math.sqrt(Number(newTempValue));
}


function play() {
    window.clearTimeout(timer);
    runFlag = 1;
    runMotion();
}

function pause() {
    window.clearTimeout(timer);
    runFlag = 0;
}


function reset() {
    window.clearTimeout(timer);
    time = 0.0;
    numBalls = 200;
    for (var i = 0; i < numBalls; i++) {
        ball[i].xValue = centerX;
        ball[i].yValue = centerY;
    }

    ball[0].deltaX = -1.0+2.0*Math.random();
    ball[0].deltaY = -1.0+2.0*Math.random();

    oldOverlap = create2DArray(numBalls, numBalls, 1)

    runFlag = 1;
    runMotion();
}
</script>



Consider a star as a singular container which holds a set of molecules together in vaccuum. By logic, we know that this structure, on it's own, does NOT hold, since, by the Ideal Gas Law,

$$PV = nRT$$

Anything which holds a certain amount of molecules, $n$, exerts an outward pressure. The intuition behind this is the consistent collisions of molecules against the walls of the container, exerting a large force per unit area which leads to an outward pressure. To counteract this pressure, we suggest that these molecules are in fact giant masses, owing to us currently exploring how a star might work. If the parts are so big, we know that there is a net inward gravitational force which suggests that we can counteract the outward pressure with "gravitational pressure". This is known as **hydrostatic equilibrium**.

A graphical representation of this can be seen below:

<p align="center">
<img src="../../../assets/preliminaries/hydrostatic.png" /><br>
<span>Figure 1.2.1 - Forces acting on our idealised depiction of a Star.</span>
</p>

## The Actual Structure of the Star

=== "$M < 0.5\text{ }M_\bigodot$"
    ![](../../../assets/preliminaries/low_mass_star_comp.png)


=== "$0.5\text{ }M_\bigodot < M < 1.5\text{ }M_\bigodot$"
    ![](../../../assets/preliminaries/mid_mass_star_comp.png)

=== "$M > 1.5\text{ }M_\bigodot$"
    ![](../../../assets/preliminaries/high_mass_star_comp.png)

<p align="center">
<span>Figure 1.2.2 - The Composition of a Star.</span>
</p>

### The Core

The core is the site of true **nuclear fusion**. This is where nuclear processes such as the **proton-proton chain**, **CNO cycle** and **triple alpha process** take place.

Notably, based on the logic of hydrostatic equilibrium, gravitational force compresses the star consistently, which means that the pressure at the centre of the star is the largest, which also means that the core itself becomes much hotter, which results in the highest star temperature being found in the core, which is helpful for nuclear fusion as well.

The following is a brief summary of the different types of Nuclear Reactions:

=== "PP Chain"
#### The Proton-Proton Chain

The **proton-proton chain** takes place in almost all stars. Based on the process of _hydrogen burning_ in order to form Helium gas, 

=== "CNO Cycle"
    #### The CNO Cycle

=== "Triple Alpha Process"
    #### Triple Alpha Processes



#### 







## The Key Equations
There are four key differential equations that dictate the star's evolution history.

### The Equation of Mass Continuity
Given a mass $M(r)$ is contained within a radius $r$, with density $\rho(r)$, we have:
$$
\frac{d}{dr} M(r) = 4\pi r^2 \rho(r)
$$

Nothing much is to be said here, except this result is very useful for the other 3 equations.

### The Equation of Hydrostatic Equilibrium

For the above situation, it must be balanced by an outward gas pressure $P(r)$ such that:

$$
\begin{align*}
\frac{d}{dr} P(r) &= - \rho(r) \frac{GM(r)}{r^2} \\
\text{or otherwise, }\frac{dP}{dM} &= - \frac{GM(r)}{4\pi r^4} \\
\text{We can hence solve this via:} \\
4\pi \int_0^r r^4 \frac{dP}{dr} dr &= G \int_0^M M(r) dM \\
4\pi (r^4 P(r) - 4\int_0^r r^3 P dr) &= G\frac{(M(r))^2}{2} \\ 
\end{align*}
$$

### The Equation of Energy Conservation

Given a star has some outward luminosity, $L$ for a given mass $M(r)$ of density $\rho(r)$ and energy per unit mass per unit time $\varepsilon(r)$ (which is defined based on the chemical composition and mass, density and temperature), it holds that:

$$
\begin{align*}
\frac{dL}{dr} &= 4\pi r^2 \rho(r) \varepsilon(r) \\
\text{or by Eqn 1, }\frac{dL}{dM} &= \varepsilon(r)
\end{align*}
$$

### The Equation for Radiative Energy Transfer

To represent the Temperature, $T(r)$ of this given star, based on the radiative energy transferred to that distance, in addition some radiative resistance $\kappa(r)$,

$$
\begin{align*}
\frac{d}{dr} T(r) &= - \frac{3\kappa(r)\rho(r)L(r)}{16\pi r^2 ac (T(r))^3} \\
\text{or by Eqn 1, }\frac{dT}{dM} &= -\frac{3\kappa(r)L(r)}{64\pi^2 acr^4 (T(r))^3}
\end{align*}
$$


## The History of the Stellar Structure

While we may now have a **much** better understanding of stars, stars we've never been to or "in", for that matter, that wasn't the case even a century ago. In Einstein's time, the idea that the Sun was powered by a core where the very elements of Hydrogen came together in the proton-proton chain would be considered blasphemous.

![Cecilia Payne (https://physicsworld.com/a/cecilia-payne-gaposchkin-the-woman-who-found-hydrogen-in-the-stars/)](../../assets/preliminaries/cecilia_payne.jpeg){ width="150", align=right }

Cecilia Payne was the true source behind our understanding of the stellar structure, an outspoken voice and truly extraordinary brain who, despite being bogged down by the then-sexist ideals of male supremacy, was able to not just make a crucial discovery, but also explain it in a way perhaps not done before.

In Stellar Spectroscopy, we follow the concept of **spectra**, which are crucial in not just seeing the variation of light but also in identifying specific elements that the origin is made of. Ideally any specific source should ideally send a continuous spectrum of different lights, which looks as follows:



However, when you notice the spectra from the Sun itself, something starts making lesser sense.


Why are there so many black lines? Why isn't it just blatantly continuous?


Well, simply put, 