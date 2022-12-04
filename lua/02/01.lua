local opp_points = {
	["A"] = 1,
	["B"] = 2,
	["C"] = 3,
}

local me_points = {
	["X"] = 1,
	["Y"] = 2,
	["Z"] = 3,
}

local result_points = {
	[0] = function()
		return 3
	end,
	[1] = function()
		return 0
	end,
	[2] = function()
		return 6
	end,
}

local function calc_outcome_points(opp, me)
	local opp_points = opp_points[opp]
	local me_points = me_points[me]
	print('opp move:', opp, 'opp points:', opp_points)
	print('me move:', me, 'me points:', me_points)
	local diff = (opp_points - me_points) % 3
	return result_points[diff]()
end

local function calc_hand(opp, me)
	local shape_points = me_points[me]
	local outcome_points = calc_outcome_points(opp, me)
	print('shape points:', shape_points)
	print('outcome points:', outcome_points)
	return shape_points + outcome_points
end

local function split_str(inputstr, sep)
	if sep == nil then
		sep = "%s"
	end
	local t = {}
	for str in string.gmatch(inputstr, "([^" .. sep .. "]+)") do
		table.insert(t, str)
	end
	return t
end

local function get_input(filename)
	local lines = {}
	for line in io.lines(filename) do
		if line == 0 then
			return lines
		end
		lines[#lines + 1] = line
	end
	return lines
end

local input = get_input('input')

local sum = 0
for _, v in pairs(input) do
	print('=========== round input:', v)
	local moves = {}
	moves = split_str(v)
	local round_points = calc_hand(moves[1], moves[2])
	sum = sum + round_points
	print(sum)
end

print('sum: ', sum)
