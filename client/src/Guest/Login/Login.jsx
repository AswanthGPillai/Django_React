
const Login = () => {

    
    return (
        <div>
            <center><h1>Login</h1></center>
            <table border={1} align='center'>
                <tr>
                    <td>Email</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td>Password</td>
                    <td><input type="text" /></td>
                </tr>
                <tr>
                    <td colSpan={2} align="center">
                        <button>Submit</button>
                        <button>Reset</button>
                    </td>
                </tr>
            </table>
        </div>
    )
}

export default Login