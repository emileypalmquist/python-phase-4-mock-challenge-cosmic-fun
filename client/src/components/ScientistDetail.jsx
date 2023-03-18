import React, {useState, useEffect} from 'react'
import { useParams } from 'react-router-dom'
import PlanetCard from './PlanetCard'
import AddMission from './AddMission'
import ScientistForm from './ScientistForm'
import planet_1 from '../assets/planetImages/planetrender_1.png'
import planet_2 from '../assets/planetImages/planetrender_2.png'
import planet_3 from '../assets/planetImages/planetrender_3.png'
import planet_4 from '../assets/planetImages/planetrender_4.png'
import planet_5 from '../assets/planetImages/planetrender_5.png'
import planet_6 from '../assets/planetImages/planetrender_6.png'
import planet_7 from '../assets/planetImages/planetrender_7.png'
import planet_8 from '../assets/planetImages/planetrender_8.png'
import planet_9 from '../assets/planetImages/planetrender_9.png'
import planet_10 from '../assets/planetImages/planetrender_10.png'

function ScientistDetail() {

  const [{data: scientist, error, status}, setScientist] = useState({
      data: null,
      error: null,
      status: "pending"
  })
  const [showEdit, setShowEdit] = useState(false)

  const { id } = useParams()
  
  const fetchScientist = async () => {
      const res = await fetch(`/scientists/${id}`)
      if (res.ok) {
          const sciJSON = await res.json()
          setScientist({data: sciJSON, error: null, status: "resolved"})
      } else {
          const sciErr = await res.json()
          setScientist({data: null, error: sciErr, status: "rejected"})
      }
  }

  useEffect(() => {
    fetchScientist()
        .catch(console.error)
  }, [id])

  const planetMap = {
      planet1: planet_1,
      planet2: planet_2,
      planet3: planet_3,
      planet4: planet_4,
      planet5: planet_5,
      planet6: planet_6,
      planet7: planet_7,
      planet8: planet_8,
      planet9: planet_9,
      planet10: planet_10
  }

  function handleAddPlanet(newPlanet) {
      setScientist({
        error,
        status,
        data: {
            ...scientist,
            planets: [...scientist.planets, newPlanet]
        }
      })
  }

  function handleUpdateScientist(){
      fetchScientist()
      setShowEdit(false)
  }

  const planetCards = scientist?.planets.map(p => <PlanetCard key={p.id} planet={p} image={planetMap[p.image]}/>)
  
  if (status === "pending") return <h2>Loading...</h2>;
  if (status === "rejected") return <h2>Error: {error.error}</h2>;
  
  return (
    <div>
        <h2>Scientist Profile:</h2>
        <img src={scientist.avatar} alt={scientist.name} />
        <h3>{scientist.name}</h3>
        <h4>Field of Study: {scientist.field_of_study}</h4>
        <button onClick={() => setShowEdit(showEdit => !showEdit)}>Edit Scientist</button>
        {showEdit && <ScientistForm scientist={scientist} onScientistRequest={handleUpdateScientist} edit={true}/>}
        <hr />
        <h2>Mission Planets:</h2>
        <div className="planetList">
            {planetCards}
        </div>
        <hr />
        <AddMission onAddPlanet={handleAddPlanet} scientistId={scientist.id} />
        
    </div>
  )
}

export default ScientistDetail