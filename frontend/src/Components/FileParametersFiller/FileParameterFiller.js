import { useEffect, useState } from "react";

export const FileParameterFiller = ({ data, setData, stringArray }) => {
    const [isToggled, setIsToggled] = useState(false);

    useEffect(() => {
        console.log("Data:", data);
        console.log("StringArray:", stringArray);
    }, [data, stringArray]);

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
            {stringArray?.map((key, index) => (
                <pre key={index}>
                    {key}: <input
                        type="text"
                        value={data[key] || ""}
                        onChange={(e) => handleInputChange(key, e.target.value)}
                    />
                </pre>
            ))}
            {isToggled ? "_" : ""}
        </div>
    );
};
