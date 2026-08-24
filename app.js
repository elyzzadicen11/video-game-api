const API_URL = "https://video-game-api-nu.vercel.app";

// GET ALL VGAMES
async function loadVGames() {
    try {
        const response = await fetch(`${API_URL}/vgames`);
        const data = await response.json();
        displayVGames(data.vgames);
    }

    catch (error) {
        console.error(error);
        document.getElementById("vgameList").innerHTML = "Unable to connect to the API.";
    }
}



// DISPLAY VGAMES
function displayVGames(vgames) {
    const vgameList =
        document.getElementById("vgameList");
    vgameList.innerHTML = "";

    vgames.forEach(vgame => {
        const card = document.createElement("div");
        card.className = "vgame-card";
        card.innerHTML = `
            <div class="vgame-year">${vgame.year}</div>
            <h3>${vgame.title}</h3>
            <p class="vgame-genre">${vgame.genre}</p>
            <div class="vgame-card-p">
                <p><span>Platform:</span> ${vgame.platform}</p>
                <p><span>Rating:</span> ${vgame.rating}</p>
            </div>
            <p class="vgame-desc">${vgame.description}</p>
            <button onclick="viewVGame(${vgame.id})"> View Details</button>
        `;
        vgameList.appendChild(card);
    });
}

// FOR POP UP CLOSING
function closePopup() {
    document.getElementById("background-popup").style.display = "none";
}

document.getElementById("closePopup").onclick = closePopup;


// GET ONE VIDEO GAME
async function viewVGame(id) {

    try {
        const response = await fetch(`${API_URL}/vgames/${id}`);
        const vgame = await response.json();
        document.getElementById("popupYear").textContent = vgame.year;
        document.getElementById("popupTitle").textContent = vgame.title;
        document.getElementById("popupGenre").textContent = vgame.genre;
        document.getElementById("popupPlatform").textContent = vgame.platform;
        document.getElementById("popupRating").textContent = vgame.rating;
        document.getElementById("popupDescription").textContent = vgame.description;
        document.getElementById("background-popup").style.display = "flex";

    }

    catch (error) {
        console.error(error);
        alert("Unable to retrieve video game.");
    }

}

// SEARCH
async function searchVGames() {
    const query = document.getElementById("searchInput").value;
    if (!query) {
        loadVGames();
        return;
    }
    try {
        const response =
            await fetch(`${API_URL}/vgames/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        displayVGames(data.results);

    }
    catch (error) {
        console.error(error);
        alert("Search failed.");
    }
}





loadVGames();