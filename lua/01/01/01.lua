function get_input(filename)
	local lines = {}
	for line in io.lines(filename) do
		lines[#lines + 1] = line
	end
	return lines
end

local input = get_input('input')

local max = 0
local sum = 0
for _, v in pairs(input) do
	if v == '' then
		if sum > max then
			max = sum
		end
		sum = 0
	else
		sum = sum + tonumber(v)
	end
end

print(max)
