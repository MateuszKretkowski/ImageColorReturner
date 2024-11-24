import { useState, useEffect } from "react";
import normalmapreworked from "../images/normalmapreworked.png"
import "./gtb.css"

export const GetTextureBits = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [imgData, setImgData] = useState(normalmapreworked);

    const [data, setData] = useState({
      width: 64,
      height: 80,
      mapWidth: 4,
      mapHeight: 4,
      objectsList: [],
  });

  const [isToggled, setIsToggled] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setIsToggled((prevState) => !prevState);
    }, 460);

    return () => clearInterval(interval);
  }, []);

    const fetchData = async (param1, param2) => {
        setLoading(true);
        setError(null);
        try {
          const response = await fetch(`http://127.0.0.1:8000/get-texture-bits/?texturePath=${imgData}&
            width=${data.width}&height=${data.height}&mapWidth=${data.mapWidth}&mapHeight=${data.mapHeight}&objectsList[]=${data.objectsList}
            &objectsList[]=${data.objectsList}`);

          if (!response.ok) {
            throw new Error('Problem with fetching data');
          }
          const result = await response.json();
          setData(result);
        } catch (err) {
          setError(err.message);
        } finally {
          setLoading(false);
        }
      };

          //<div>
           // {loading && <p>Loading...</p>}
            //{error && <p>Error: {error}</p>}
            //{data && <pre>const data = {JSON.stringify(data, null, 2)}</pre>}
          //</div>

    return (
        <div className="Main">
          <div className="main_container gtb_container">
          <div className="sides-wrapper">
            <div className="left_side gtb_left_side">
              {data && <pre>const data = {JSON.stringify(data, null, 2)}{isToggled ? "_" : ""}</pre>}
            </div>
            <div className="right_side gtb_rigth_side">
            <div className="image-wrapper">
              <img src={imgData ? normalmapreworked : imgData} className="mapImage gtb_image" />
            </div>
            </div>
          </div>
            <div className="button-wrapper">
              <button onClick={() => fetchData({}, 'value2')}>Get Texture Bits</button>
            </div>
          </div>
        </div>
    )
}