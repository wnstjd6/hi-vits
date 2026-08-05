param(
    [Parameter(Mandatory=$true)] [string] $issue,
    [Parameter(Mandatory=$true)] [string] $short
)

$branch = "feat/#$issue-$short"
Write-Output "Creating branch: $branch"

git checkout -b $branch main
git push -u origin $branch

Write-Output "Branch created and pushed: $branch"
