#!/usr/bin/env python3

from kodijson import Kodi, PLAYER_VIDEO

def main():
   #Login with default kodi/kodi credentials
   kodi = Kodi("http://localhost:8080/jsonrpc")
   
   #Login with custom credentials
   #kodi = Kodi("http://YOURHOST/jsonrpc", "login", "password")
   
   # Test the access to JSON_RPC
   print(kodi.JSONRPC.Ping())
   
   # Navigate throught windows
   # Go to videos window
   kodi.GUI.ActivateWindow({"window":"videos"})
   
   #kodi.Player.SetPartymode({"playerid": 0, "partymode": True})
   #playlist = kodi.Playlist.GetPlaylists()
   #print(playlist)
   
   #items = kodi.Playlist.GetItems({"playlistid": 1})
   #print(items)
   
   # Add item to playlist
   kodi.Playlist.Clear({"playlistid": 1})
   kodi.Playlist.Add({"playlistid": 1, "item": {"musicvideoid": 1}})
   kodi.Playlist.Add({"playlistid": 1, "item": {"musicvideoid": 25}})
   kodi.Playlist.Add({"playlistid": 1, "item": {"musicvideoid": 30}})
   
   videos = kodi.VideoLibrary.GetMusicVideos()
   print(videos)
   
   players = kodi.Player.GetPlayers()
   print(players)
   
   # Open and play file
   #kodi.Player.Open({"item": {"file":"/home/luiz/bolofofos/Bolofofos - MÚSICA DE ANIVERSÁRIO.mkv"}})
   
   # Open video by musicvideoid on videoLibrary
   #kodi.Player.Open({"item": {"musicvideoid": 35}})
   
   # Open and play playlist
   kodi.Player.Open({"item": {"playlistid": 1}})
   # Show some notifiations :
   kodi.GUI.ShowNotification({"title":"Title", "message":"Hello Word, tocando bolofofos"})
   
if __name__ == "__main__":
   main()
