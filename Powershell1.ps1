
$recentfiles=(ls . -File -Recurse | where {$_.LastWriteTime -ge (get-date).AddHours(-2)})

foreach ($file in $recentfiles) {

if ($file.Length -ge 1mb) { 
Write-host $file.Name is $file.Length bytes 
}}
