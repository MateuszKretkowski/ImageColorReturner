import { useEffect, useState } from "react";

export const FileParameterFiller = ({ data, setData, stringArray, lastIndex }) => {
    const [isToggled, setIsToggled] = useState(false);

    useEffect(() => {
        const interval = setInterval(() => {
            setIsToggled((prevState) => !prevState);
        }, 460);

        return () => clearInterval(interval);
    }, []);

    const handleInputChange = (key, value) => {
        setData((prevData) => ({
            ...prevData,
            [key]: value,
        }));
    };

    return (
        <div className="fpf">
            <span>const data = &#123;</span> {/* Wizualne {} */}
            {stringArray?.map((key, index) => (
                <pre className="fpf_pre" key={index}>
                    {/* Jeśli to nie ostatni element, renderujemy input */}
                    {index !== stringArray.length - 1 && (
                        <>
                            {key}: <input
                                type="text"
                                value={data[key] || ""}
                                onChange={(e) => handleInputChange(key, e.target.value)}
                            />
                        </>
                    )}
    
                    {/* Jeśli to ostatni element, renderujemy przycisk */}
                    {index === stringArray.length - 1 && (
                        <>
                        {key}: <button className="small_btn">Add New Object</button>
                        </>
                    )}
                </pre>
            ))}
            <span>&#125;</span> {/* Wizualne zamknięcie nawiasu */}
            {isToggled ? "_" : ""}
        </div>
    );
};
