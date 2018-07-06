
# coding: utf-8

# In[11]:


#set 1
set1={'a','b','c','f','s','g'};
#set 2
set2={'a','c','t','f','b','z','y'};
print("\n\nSet 1 is : ",set1);
print("\n\nSet 2 is : ",set2);
    
set3=set1|set2;     #set1.union(set2)
print("\nUnion of set1 and set2 : ",set3);

set4=set1&set2;     #set1.intersection(set2)
print("\nIntersection of set1 and set2 : ",set4);

set5=set1.difference(set2);
print("\nDifference of set1 and set2 (set1-set2) is : ",set5);

set6=set1.symmetric_difference(set2);
print("\nSymmetric Difference of set1 and set2 is : ",set6);

set7=set1.issubset(set2);
print("\nset1 is subset of set2 : ",set7);

set8=set1.issuperset(set2);
print("\nset1 is subset of set2 : ",set7);

set9={'a','b','c','d','e','f'};
set10={'a','b','c'};

set11=set10.issubset(set9);
print("\nset10 is subset of set9 : ",set11);

set12=set9.issuperset(set10);
print("\nset9 is superset of set10 : ",set12);

set16=set10.isdisjoint(set9);
print("\nset9 and set10 are disjoint : ",set16);


set13={'a','b','c'};
set14={'d','e','f'};

set15=set13.isdisjoint(set14);
print("\nset1 and set2 are disjoint : ",set15);

