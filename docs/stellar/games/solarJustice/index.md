Solar Justice
=============

1.  Start with Player 1 (**Star**) placing a **star** in the grid.
2.  Player 2 (**Stellar Wind**) gusts in any of the 8 directions. Once passed, mark it as completed.
3.  **Gas clouds** drop in the direction of the **Stellar Wind**.
4.  **Stars** can plant **stars** on existing **Gas clouds**.
5.  Run (2) to (4) seven times (i.e. drop 7 **stars** on the board, all except one direction of **stellar wind** used).
6.  If there are any empty spaces at the end, Player 2 wins. Otherwise, Player 1 wins.

Play the real game [here](./real.html).


<div class="solar_justice_game_board">
    <div class="solar_justice_child">
        <table id="solar_justice_grid" class="solarJustice"></table>
    </div>
    <div class="solar_justice_child">
        <table id="solar_justice_compass" class="solarJustice"></table>
    </div>
</div>

<script>
var grid = new Array(5);
var starTurn = true;

for (var i = 0; i < 5; i++) {
    grid[i] = new Array(5);
    for(let j = 0; j < 5; j++) {
        grid[i][j] = "🌌";
    }
}

var starPosn = [];

var directions = new Map();
["N", "S", "E", "W", "NE", "NW", "SE", "SW"].forEach(
    (value, _, _2) => {
        directions.set(value, false);
    }
)


function drawGrid(gridTbl) {
    gridTbl.innerHTML = "";
    for(let i = 0; i < 5; i++) {
        const tr = gridTbl.insertRow();
        for(let j = 0; j < 5; j++) {
            let td = tr.insertCell();
            td.classList.add("solarJustice");
            // td.style.backgroundColor = grid[i][j] != "🌞" ? "#fff" : "#f70d1a"; // Green: #57f962
            td.appendChild(document.createTextNode(grid[i][j]));
            td.addEventListener("click", (_) => {
                if(starTurn == true && grid[i][j] != "🌞") {
                    grid[i][j] = "🌞"
                    td.innerHTML = "";
                    td.appendChild(document.createTextNode(grid[i][j]));
                    starTurn = false;
                    starPosn.push([i, j]);
                }
            } );
        }
    }
}


const body = document.body;

const gridTbl = document.getElementById("solar_justice_grid");
drawGrid(gridTbl);
//body.appendChild(gridTbl);

function fillWind(dirn) {
    starPosn.forEach(
        (value, index, array) => {
            let i = value[0], j = value[1];
            if(dirn == "N") {
                for(let x = 0; x < i; x++) grid[x][j] = "⛅"; 
            } else if(dirn == "S") {
                for(let x = i+1; x < 5; x++) grid[x][j] = "⛅"; 
            } else if(dirn == "W") {
                for(let x = 0; x < j; x++) grid[i][x] = "⛅"; 
            } else if(dirn == "E") {
                for(let x = j+1; x < 5; x++) grid[i][x] = "⛅"; 
            } else if(dirn == "NE") {
                for(let x = i-1, y = j+1; -1 < x && y < 5; x--, y++) { grid[x][y] = "⛅"; }
            } else if(dirn == "SE") {
                for(let x = i+1, y = j+1; x < 5 && y < 5; x++, y++) { grid[x][y] = "⛅"; }
            } else if(dirn == "NW") {
                for(let x = i-1, y = j-1; -1 < x && -1 < y; x--, y--) { grid[x][y] = "⛅"; }
            } else if(dirn == "SW") {
                for(let x = i+1, y = j-1; x < 5 && -1 < y; x++, y--) { grid[x][y] = "⛅"; }
            }
        }
    )
    starPosn.forEach(
        (value, _, _2) => {
            let i = value[0], j = value[1];
            grid[i][j] = "🌞";
        }
    )
    drawGrid(gridTbl);
}

function checkWhoWon() {
    for(let i = 0; i < 5; i++) {
        for(let j = 0; j < 5; j++) {
            if(grid[i][j] == "🌌") return "Wind";
        }
    }
    return "Star";
}

const compassTbl = document.getElementById("solar_justice_compass");

for (let i = 0; i < 3; i++) {
    const tr = compassTbl.insertRow();
    for (let j = 0; j < 3; j++) {
        const td = tr.insertCell();
        td.classList.add("solarJustice");
        let dirn = i == 1 && j == 1 ? "🧭" : ((i+j)%2 == 1 ? (j == 1 ? (i == 0 ? "N" : "S") : (j == 0 ? "W" : "E")): (i==0 ? "N" : "S") + (j==0 ? "W" : "E"));
        td.appendChild(document.createTextNode(dirn));
        td.addEventListener("click", (_) => {
            if(!starTurn && !directions.get(dirn)) { 
                directions.set(dirn, true);
                td.style.backgroundColor = "#f70d1a"; 
                fillWind(dirn);
                starTurn = true;
                if(Array.from(directions.values()).reduce((prev, current) => prev + current, 0) == 7) alert(checkWhoWon()+" won!");
            }
        } );
    }
}

</script>