param (
    [String]$ImagePath
)

"Inputted image: $ImagePath`nOriginal Hash: " + (Get-FileHash $ImagePath).Hash | Out-File hash.txt

