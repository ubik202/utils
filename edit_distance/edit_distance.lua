-- Distance: edit distance from string given in config
--
--

function dump(o)
   if type(o) == 'table' then
      local s = '{ '
      for k,v in pairs(o) do
         if type(k) ~= 'number' then k = '"'..k..'"' end
         s = s .. '['..k..'] = ' .. dump(v) .. ','
      end
      return s .. '} '
   else
      return tostring(o)
   end
end



function clone_array(arr)
  local result = {}
  for i = 1, #arr do
      result[i] = arr[i]
  end
  return result
end

function edit_distance(string1,string2)
    local m = #string1
    local n = #string2
    local d = {}
    local temp = {}
    for i = 1, n+2 do
       temp[#temp+1]=0;
    end
    for i = 1, m+2 do 
       d[#d+1] = clone_array(temp)
    end
    for i = 1, m+2 do 
       d[i][1] = i-1
    end
    for i = 1, n+2 do 
       d[1][i] = i-1
    end
    for j = 2, n+2 do
        for i = 2, m+2 do
           if(string1[i-1] == string2[j-1]) then
               d[i][j] = d[i-1][j-1]           
           else
               d[i][j] = math.min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1 )
           end
        end     
    end
    return d[m][n]
end

getmetatable('').__index = function(str,i) return string.sub(str,i,i) end
for i = 1, #tuple do
    return(edit_distance(get_config("reference_string"),tuple[i].value))
end
