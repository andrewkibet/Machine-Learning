function Submit()
{
    let diamter=document.getElementById("diameter").value;
    let weight=document.getElementById("weight").value;
    let red=document.getElementById("red").value;
    let blue=document.getElementById("blue").value;
    let green=document.getElementById("green").value;
    let result=document.getElementById("result")

    let data={'diameter':diamter,"weight":weight,"red":red,"blue":blue,"green":green}

    url="http://127.0.0.1:5000/model/api"

    axios.post(url,data)
    .then((res)=>{
        console.log(res.data)
        result.innerHTML=res.data

    })
    .catch((err)=>{


    })
    
    console.log(data)
    console.log(data['red'])
}