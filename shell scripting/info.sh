if [ -z "$1" ]; then
  echo "Usage: $0 <csv_url>"
  exit 1
fi

URL="$1"

curl -s "$URL" \
| csvcut -c "Security","Headquarters Location","Founded" --encoding latin1 \
| csvsort -c Founded \
| tail -n +2 \
| awk -F',' '
{
  printf "%s, %s, %s\n", $1, $2, $3
}
'
