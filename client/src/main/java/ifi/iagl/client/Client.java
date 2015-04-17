package ifi.iagl.client;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Calendar;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import proto.AckProto.Ack;
import proto.TweetProto.Tweet;
import proto.UserProto.User;

/**
 * Client side to send message via console
 */
public class Client {
	/**
	 * Pattern of correct message input
	 */
	private static final String PATTERN_USERNAME = "\\p{Alnum}+";
	private static final String PATTERN_MESSAGE = "^@(" + PATTERN_USERNAME + ")?\\s+(.*)$";

	/**
	 * The current user
	 */
	private static User me;

	/**
	 * Default settings for server connection
	 */
	private static final Integer DEFAULT_PORT = 10000;
	private static final String DEFAULT_IP = "127.0.0.1";
	private static final Integer DEFAULT_TIMEOUT = 5000;

	private static final Integer MAX_CHAR = 140;

	public static void main(String argv[]) {
		String username = null;
		Integer port = DEFAULT_PORT;
		String ip = DEFAULT_IP;
		Integer timeout = DEFAULT_TIMEOUT;

		Boolean valid = true;

		switch (argv.length) {
		case 4:
			try {
				timeout = Integer.parseInt(argv[3]);
			} catch (NumberFormatException ex) {
				System.err.println("Timeout must be a valid integer");
				valid = false;
			}
		case 3:
			ip = argv[2];
		case 2:
			try {
				port = Integer.parseInt(argv[1]);
			} catch (NumberFormatException ex) {
				System.err.println("Port must be a valid integer");
				valid = false;
			}
		case 1:
			if (!argv[0].matches(PATTERN_USERNAME)) {
				System.err.println("username must be alphanumeric only");
				valid = false;
			} else {
				username = argv[0];
			}
			break;
		default:
			valid = false;
			break;
		}
		if (valid) {
			me = User.newBuilder().setUsername(username).build();
			Ack ack; // response from server
			System.out.println(String.format("\n - Welcome %s !\n # Message (%d charaters max) will be send to %s:%d (waiting %d ms for the ack)\n", username, MAX_CHAR, ip, port, timeout));
			try (Scanner scan = new Scanner(System.in)) {
				while (true) {
					System.out.print(">>");
					String input = scan.nextLine();
					if (input.length() > MAX_CHAR) {
						System.out.println(" # Message too long (max: " + MAX_CHAR + ")");
					} else {
						ack = send(ip, port, timeout, input);
						System.out.println(String.format("<< [%s] %s", ack.getStatus(), ack.getMessage()));
					}
				}
			} catch (NoSuchElementException ex) {
				System.out.println("\n" + " - Bye !");
			} catch (Exception e) {
				System.out.println("\n# ERROR " + e.getMessage() + "\n");
				e.printStackTrace();
			}
		} else {
			usage();
		}
	}

	/**
	 * Print description of arguments
	 */
	private static void usage() {
		System.out.println("- Aguments invalid : username [port [ip [timeout]]");
		System.out.println(String.format("- Default value :\n # port %d\n # ip %s\n #timeout %d", DEFAULT_PORT, DEFAULT_IP, DEFAULT_TIMEOUT));
	}

	/**
	 * Send the message to the server
	 * 
	 * @param ip
	 *            IP of the server
	 * @param port
	 *            port of the server
	 * @param timeout
	 *            timeout of connection
	 * @param content
	 *            message to send
	 * @return The Ack of the server
	 * @throws UnknownHostException
	 *             from {@link Socket#Socket(String, int)}
	 * @throws IOException
	 *             from {@link Socket#Socket(String, int)}s
	 */
	public static Ack send(String ip, int port, int timeout, String content) throws UnknownHostException, IOException {

		Tweet.Builder tweetBuilder = Tweet.newBuilder();
		tweetBuilder.setTimestamp(Calendar.getInstance().getTimeInMillis()).setSender(me);

		// check receiver of the message
		Matcher matcher = Pattern.compile(PATTERN_MESSAGE).matcher(content);
		if (matcher.matches()) {
			tweetBuilder.setReceiver(User.newBuilder().setUsername(matcher.group(1)).build()).setMessage(matcher.group(2));
		} else {
			// to everyone
			tweetBuilder.setMessage(content);
		}

		Tweet tweet = tweetBuilder.build();
		Ack ack;

		// open a socket on the server and try to send the tweet
		try (Socket clientSocket = new Socket(ip, port); DataOutputStream toServer = new DataOutputStream(clientSocket.getOutputStream())) {
			tweet.writeTo(toServer);
			clientSocket.setSoTimeout(timeout);
			ack = Ack.parseFrom(clientSocket.getInputStream());
		} catch (Exception exc) {
			throw exc;
		}

		return ack;
	}
}