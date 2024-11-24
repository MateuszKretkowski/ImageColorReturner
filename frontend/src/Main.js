
import { useNavigate } from "react-router-dom"
export const Main = () => {
    const nav = useNavigate();
    return (
        <div>
            <h1>Main page</h1>
            <button onClick={() => {nav('/items')}}>Items</button>
           
      </div>
    )
}