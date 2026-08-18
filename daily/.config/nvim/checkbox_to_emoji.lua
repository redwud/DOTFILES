-- checkbox_to_emoji.lua
-- Replaces all "[x]" occurrences in the current buffer with "✅"
-- and strips 4 leading spaces from every line.
-- Usage from Neovim command line: :luafile %
-- Or via the :CheckboxToEmoji command (registered in init.lua)

local function checkbox_to_emoji()
  local buf = vim.api.nvim_get_current_buf()
  local lines = vim.api.nvim_buf_get_lines(buf, 0, -1, false)

  local changed = 0
  for i, line in ipairs(lines) do
    local new_line = line:gsub("^    ", ""):gsub("%[x%]", "✅"):gsub("%[ %] ","")
    if new_line ~= line then
      lines[i] = new_line
      changed = changed + 1
    end
  end

  vim.api.nvim_buf_set_lines(buf, 0, -1, false, lines)
  vim.notify(string.format("checkbox_to_emoji: updated %d line(s)", changed))
end

checkbox_to_emoji()
