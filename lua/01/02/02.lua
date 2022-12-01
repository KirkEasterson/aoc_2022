function get_input(filename)
	local lines = {}
	for line in io.lines(filename) do
		lines[#lines + 1] = line
	end
	return lines
end

local input = get_input('input')

local totals = {}
local sum = 0
for _, v in pairs(input) do
	if v == '' then
		totals[#totals + 1] = sum
		sum = 0
	else
		sum = sum + tonumber(v)
	end
end

table.sort(totals, function(a, b) return a > b end)
print(totals[1])
print(totals[2])
print(totals[3])

top_three = totals[1] + totals[2] + totals[3]
print('top three total: '..top_three)
