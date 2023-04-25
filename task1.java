package For_java_HW;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class task1{
    

    public static void addNumber(String key, int value, Map<String, ArrayList<Integer>> map){
        if (map.containsKey(key)) {
            map.get(key).add(value);
 } else {
            ArrayList<Integer> list = new ArrayList<>();
            list.add(value);
            map.put(key, list);
        }

    }
    
    public static void printBook(Map<String, ArrayList<Integer>> map){
        for (var item : map.entrySet()) {
            String phones = "";
            for(int el: item.getValue()){
                phones = phones + el + ", ";
            }
            System.out.printf("%s: %s \n", item.getKey(), phones);
        }
    }
    public static void main(String[] args) {
        Map<String, ArrayList<Integer>> bookPhone = new HashMap<>();
        addNumber("Morozov", 749390, bookPhone);
        addNumber("Morozov", 4593386, bookPhone);
        addNumber("Petrov", 926549, bookPhone);
        addNumber("Popov", 956875734, bookPhone);
        addNumber("Popov", 48363842, bookPhone);
        addNumber("Dobro", 9787667, bookPhone);
        printBook(bookPhone);
       }
}