class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String ,List<String>> res = new HashMap<>();
        for(String s : strs)
        {
            char[] Sarr = s.toCharArray();
            Arrays.sort(Sarr);
            String srtd = new String(Sarr);
            res.putIfAbsent(srtd, new ArrayList<>());
            res.get(srtd).add(s);

        }
        return new ArrayList<>(res.values());
    }
}
