import { useState } from "react";
import normalmapreworked from "../images/normalmapreworked.png";
import { FileParameterFiller } from "../FileParametersFiller/FileParameterFiller";
import "./gtb.css";

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

    const fetchData = async () => {
        setLoading(true);
        setError(null);

        try {
            const params = new URLSearchParams({
                texturePath: imgData,
                width: data.width,
                height: data.height,
                mapWidth: data.mapWidth,
                mapHeight: data.mapHeight,
            });

            // Dodaj obiekty z `objectsList` jako osobne parametry
            data.objectsList.forEach((item, index) => {
                params.append(`objectsList[${index}]`, item);
            });

            const response = await fetch(`http://127.0.0.1:8000/get-texture-bits/?${params.toString()}`);

            if (!response.ok) {
                throw new Error("Problem with fetching data");
            }

            const result = await response.json();
            setData(result);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="Main">
            <div className="main_container gtb_container">
                <div className="sides-wrapper">
                    <div className="left_side gtb_left_side">
                        <FileParameterFiller
                            data={data}
                            setData={setData}
                            stringArray={["width", "height", "mapWidth", "mapHeight", "objectsList"]}
                        />
                    </div>
                    <div className="right_side gtb_rigth_side">
                        <div className="image-wrapper">
                            <img
                                src={imgData ? normalmapreworked : imgData}
                                className="mapImage gtb_image"
                                alt="Texture"
                            />
                        </div>
                    </div>
                </div>
                <div className="button-wrapper">
                    <button onClick={fetchData} disabled={loading}>
                        {loading ? "Loading..." : "Get Texture Bits"}
                    </button>
                </div>
                {error && <p className="error">Error: {error}</p>}
            </div>
        </div>
    );
};
