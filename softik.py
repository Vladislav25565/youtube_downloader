def povareshka():
  video = YouTube(link)
  stream = video.streams.get_highest_resolution()
  stream.download()

from pytube import YouTube
link = input("Enter URL of Video\n")
print(f"This link: {link}")
abcd = input("Are you sure\n")
if abcd == "yes":
  povareshka()
if abcd == "Yes":
  povareshka()
if abcd == "YES":
  povareshka()
