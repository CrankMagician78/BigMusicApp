function go_to(tab){
    var home = document.getElementById("home");
    var artist = document.getElementById("artist");
    var album = document.getElementById("album");
    var song = document.getElementById("song");
    var playlist = document.getElementById("playlist");
    home.style.display = "none";
    artist.style.display = "none";
    album.style.display = "none";
    song.style.display = "none";
    playlist.style.display = "none";

    switch(tab){
        case "home":
            home.style.display = "flex";
        case "artist":
            artist.style.display = "flex";
        case "album":
            album.style.display = "flex";
        case "song":
            song.style.display = "flex";
        case "playlist":
            playlist.style.display = "flex";
    }
}
