import sys

class Node:
    def __init__(self,parent,state,g,d,f,isUninformed):
        self.parent=parent
        self.state=state
        self.g=g
        self.d=d
        self.f=f
        self.isUninformed=isUninformed

def ReadFile(filename):
    file=open("./input1.txt","r")
    dict={}
    for line in file:
        line=line.rstrip("\n")
        line=line.rstrip("\r")
        if line=="END OF INPUT":
            return dict
        else:
            data=line.split(" ")
            #This is for checking if data[0] in the list for data[0]->data[1] i.e city1->city2
            if (data[0] in dict):
                dict[data[0]].append([data[1],float(data[2])]) #Appending Lukurmbeg:[Hamburg,63]
            else:
                dict[data[0]]=[[data[1],float(data[2])]] #If not present adding them as a list to the data[0]:[data[1],distance]
            #This is for checking if data[1] in the list for data[1]->data[0] i.e city2->city1
            if (data[1] in dict):
                dict[data[1]].append([data[0],float(data[2])]) #Appending Lukurmbeg:[Hamburg,63]
            else:
                dict[data[1]]=[[data[0],float(data[2])]] #If not present adding them as a list to the data[0]:[data[1],distance]
    print('Please do add "END OF INPUT" to the end of your input file')

def ReadHueresticFile(filename):
    file=open(filename,"r")
    dict={}
    for line in file:
        line=line.rstrip("\n")
        line=line.rstrip("\r")
        if line=="END OF INPUT":
            return dict
        else:
            data=line.split(" ")
            dict[data[0]]=float(data[1])
    print('Please do add "END OF INPUT" to the end of your input file')  

def Expand(node,dict,huerestic): #to generate the sucessor function
    successorFunction=[]
    curNodeData=dict[node.state]
    dist=0
    for data in curNodeData:
        if node.isUninformed:
            dist=node.g+float(data[1])
            successorFunction.append(Node(node,data[0],dist,node.d+1,0,True))
        else:
            dist=node.g+float(data[1])+float(huerestic[data[0]])
            successorFunction.append(Node(node,data[0],float(dist-huerestic[data[0]]),node.d+1,dist,False))
    return successorFunction

def Routes(dict,node):
    distance=node.g
    routes=[]
    while node.parent is not None:
        parent=node.parent
        for a in dict[parent.state]:
            if a[0] == node.state:
                routes.append(parent.state+" to "+node.state+"->"+str(a[1])+"Km")
        node=parent
    routes.reverse()#As we move backwards looking for each of the parents untill
                    #reaching the node whose parents are null i.e the root node
    print("Distance:"+str(distance))
    for route in routes:
        print(route)


def main():
    dict={}
    count=0
    heursticdict={}
    fringe=[]
    closed=[]
    nodesPopped=0
    nodesGenerated=0
    nodesExpanded=0
    length=len(sys.argv)
    if(length==4):
        isUninformed=True
    elif(length==5):
        isUninformed=False
    else:
        print("Please provide command in this format: find_route input_filename origin_city destination_city <heuristic_filename>")
        return
    
    dict=ReadFile(sys.argv[1])

    if not isUninformed:
        heursticdict=ReadHueresticFile(sys.argv[4])
    
    #Then add the first value from the input command to the fringe and closed is empty as it is initialized earlier
    if isUninformed:
        fringe.append(Node(None,sys.argv[2],0,0,0,isUninformed))
    else:
        fringe.append(Node(None,sys.argv[2],0,0,heursticdict[sys.argv[2]],isUninformed))
    nodesGenerated+=1
    while (len(fringe)>0):
        curNode=fringe.pop(0) #Removes the first element on the stack
        nodesPopped+=1
        if(curNode.state ==sys.argv[3]):
            count+=1
            print("Nodes Generated: "+str(nodesGenerated))
            print("Nodes Popped: "+str(nodesPopped))
            print("Nodes Expanded: "+str(nodesExpanded))
            Routes(dict,curNode)
            sys.exit()
        else:
            if(curNode.state not in closed):
                closed.append(curNode.state)
                nodesExpanded+=1
                successor=Expand(curNode,dict,heursticdict)
                for succ in successor:
                    fringe.append(succ)
                    nodesGenerated+=1
                fringe.sort(key=lambda x: x.g, reverse=False)
            else:
                if(curNode==sys.argv[2]):
                    break;
    #If it reaches here then its is not found any route
    print("Nodes Generated: "+str(nodesGenerated))
    print("Nodes Popped: "+str(nodesPopped))
    print("Nodes Expanded: "+str(nodesExpanded))
    print("Route : Infinity(No routes found)")    

           



                
if __name__=="__main__":
    main()




    
