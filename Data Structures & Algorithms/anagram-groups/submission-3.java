class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
       HashMap<String, ArrayList<String>> res = new HashMap<>();
        for(String s : strs){
           char[] sorted = s.toCharArray();
           Arrays.sort(sorted);
           String ss = new String(sorted);
           res.putIfAbsent(ss, new ArrayList<String>());
           res.get(ss).add(s);
        }
        return new ArrayList<>(res.values());
    }
}
